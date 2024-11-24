# Defineerime vahemiku [-MAX, MAX]
MAX = 10  # Maksimaalne väärtus, mida saame käsitleda (vahemik [-10, 10])
mapping = [False] * (2 * MAX + 1)  # Loome massiivi suurusega 21, et pidada järge väärtuste olemasolu kohta.

# Funktsioon väärtuse märkimiseks
def mark_value(val):
    mapping[val + MAX] = True  # Märgime vastava väärtuse "aktiivseks", teisendades selle indeksiks (val + MAX).

# Funktsioon olemasolu kontrollimiseks
def check_value(val):
    return mapping[val + MAX]  # Tagastab, kas vastav väärtus on märgitud (True/False).

# Märgime mõned väärtused
mark_value(3)      # Märgib väärtuse 3 (massivi indeksis 3 + 10 = 13 väärtus muutub True'ks).
mark_value(-5)     # Märgib väärtuse -5 (massivi indeksis -5 + 10 = 5 väärtus muutub True'ks).

# Kontrollime väärtuste olemasolu
print(check_value(3))  # Kontrollib, kas 3 on märgitud (indeksis 13). Tulemus: True.
print(check_value(7))  # Kontrollib, kas 7 on märgitud (indeksis 17). Tulemus: False.


# 2. Aja- ja ruumikomplekssus

# Ajakulu:
# Märkimine ja kontrollimine: O(1) (otsene juurdepääs indeksile).
# Eelised: Väga kiire.
# Puudused: Sobib ainult fikseeritud ja väikese vahemiku jaoks.
# Ruumikulu: O(m) (massiiivi suurus, kus  m on vahemiku suurus).

# 3. Rakendus reaalses maailmas
# Bitikaardid: Andmete olemasolu kiireks kontrollimiseks (nt Bloomi filtrites).
# Unikaalsete väärtuste salvestamine: Väikese vahemiku väärtuste kiire otsimine.
# Numbripõhine loendus: Näiteks eksamite punktide sageduse salvestamine.