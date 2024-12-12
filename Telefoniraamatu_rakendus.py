
import json  # impordime json-mooduli

# kontaktide andmete salvestamise fail
FAILINIMI = "kontaktid.json"

# salvestab kontaktid faili
def salvesta_kontaktid(failinimi, kontaktid):
    with open(failinimi, 'w', encoding='utf-8') as fail:
        json.dump(kontaktid, fail, ensure_ascii=False)

# laadib kontaktid failist
def lae_kontaktid(failinimi):
    try:
        with open(failinimi, 'r', encoding='utf-8') as fail:
            return json.load(fail)
    except FileNotFoundError:
        return []

# lisab uue kontakti
def lisa_kontakt(kontaktid, nimi, telefon):
    kontaktid.append({"nimi": nimi, "telefon": telefon})
    salvesta_kontaktid(FAILINIMI, kontaktid)
    print(f"Kontakt '{nimi}' lisatud!")

# otsib kontakti binaarse otsinguga
def binaarne_otsing(kontaktid, nimi):
    vasak, parem = 0, len(kontaktid) - 1
    while vasak <= parem:
        kesk = (vasak + parem) // 2
        if kontaktid[kesk]['nimi'] == nimi:
            return kontaktid[kesk]
        elif kontaktid[kesk]['nimi'] < nimi:
            vasak = kesk + 1
        else:
            parem = kesk - 1
    return None

# sorteerib kontaktid kiire sorteerimisega
def kiire_sortimine(kontaktid):
    if len(kontaktid) <= 1:
        return kontaktid
    else:
        pivot = kontaktid[0]
        väiksemad = [x for x in kontaktid[1:] if x['nimi'] <= pivot['nimi']]
        suuremad = [x for x in kontaktid[1:] if x['nimi'] > pivot['nimi']]
        return kiire_sortimine(väiksemad) + [pivot] + kiire_sortimine(suuremad)

# kuvab kõik kontaktid
def kuva_kontaktid(kontaktid):
    if not kontaktid:
        print("kontaktide nimekiri on tühi.")
    else:
        for kontakt in kontaktid:
            print(f"nimi: {kontakt['nimi']}, telefon: {kontakt['telefon']}")

# peamenüü funktsioon
def menuu():
    kontaktid = lae_kontaktid(FAILINIMI)
    while True:
        print("\n--- telefoniraamatu rakendus ---")
        print("1. lisa kontakt")
        print("2. otsi kontakti")
        print("3. kuva kõik kontaktid")
        print("4. välju")
        valik = input("vali toiming (1-4): ")

        if valik == "1":
            nimi = input("sisesta nimi: ")
            telefon = input("sisesta telefoninumber: ")
            lisa_kontakt(kontaktid, nimi, telefon)
            kontaktid = kiire_sortimine(kontaktid) # sorteerib kontaktid pärast lisamist
        elif valik == "2":
            otsitav_nimi = input("sisesta otsitava kontakti nimi: ")
            tulemus = binaarne_otsing(kontaktid, otsitav_nimi)
            if tulemus:
                print(f"leitud kontakt - nimi: {tulemus['nimi']}, telefon: {tulemus['telefon']}")
            else:
                print("kontakti ei leitud.")
        elif valik == "3":
            kuva_kontaktid(kontaktid)
        elif valik == "4":
            print("rakendus suletakse. Head päeva!")
            break
        else:
            print("imelik valik, proovi uuesti.")

# käivitab menüü
if __name__ == "__main__":
    menuu()
