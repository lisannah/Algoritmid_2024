def binaarne_otsing(numbrid, siht):
  
    vasak, parem = 0, len(numbrid) - 1  # Määrame vasaku ja parema piiri, et alustada otsingut

    while vasak <= parem:  # Kuniks vasak piir on väiksem või võrdne paremale piirile
        keskmine = (vasak + parem) // 2  # Arvutame keskmise indeksi
        
        if numbrid[keskmine] == siht:  # Kontrollime, kas keskmine element on meie sihtnumber
            return keskmine  # Tagastame keskmise indeksi, kui number leiti
        elif numbrid[keskmine] < siht:  # Kui keskmine element on väiksem kui siht
            vasak = keskmine + 1  # Liigutame otsingut edasi paremale (uuendame vasaku piiri)
        else:  # Kui keskmine element on suurem kui siht
            parem = keskmine - 1  # Liigutame otsingut edasi vasakule (uuendame parema piiri)

    return -1  # Tagastame -1, kui number ei leitud

# Testime
sorteeritud_numbrid = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] 
otsitav_number = 5  
indeks = binaarne_otsing(sorteeritud_numbrid, otsitav_number)  # Käivitame binaarse otsingu funktsiooni

# Kontrollime, kas indeks ei ole -1 (tähendab, et number leiti)
if indeks != -1:  
    print(f"Leitud number {otsitav_number} indeksil {indeks}.")  # Kuvame leitud numbri indeksi
else:
    print(f"Number {otsitav_number} pole loendis.")  # Kuvame sõnumi, et number ei leitud
