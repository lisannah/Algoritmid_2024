Ülesanne 4: Kolmikotsing ja Kahendotsing 


Ternary Search ülevaade ja põhiprintsiibid:

Ternary Search on algoritm sorteeritud massiivide jaoks, mis jagab massiivi iga kord kolmeks:
1. Leiab kaks võrreldavat punkti mid1 ja mid2.
2. Võrdleb otsitavat väärtust x nendega
Seda kasutatakse ülesandes,kus on vaja leida näiteks minimaalne või maksimaalne väärtus, kõige odavam hind, kõige lühem tee või kõige efektiivsem lahendus.


Ternary pseudo-kood:

Alusta otsingut, kasutades vasakut ja paremat piiri.
Arvuta kaks punkti, mida nimetame m1 ja m2, et jagada otsinguväli kolmeks.
Võrdle funktsiooni väärtusi punktides m1 ja m2.
Kui f(m1) on väiksem kui f(m2), siis liiguta vasakut piiri m1 juurde.
Kui f(m2) on väiksem või võrreldav, siis liiguta paremat piiri m2 juurde.
Korda neid samme, kuni vasaku ja parema piiri vaheline kaugus on väiksem kui määratud täpsus.
Tagasta vahemiku keskmine punkt, mis on kõige lähemal optimaalsele lahendusele.



Ternary Search vs Binary Search ajakeerukus:

Binary Search: O(log⁡2n)
Ternary Search: O(log⁡3n)
Ajakeerukuse poolest on ternaarne otsing teoreetiliselt veidi kiirem logaritmi baasi tõttu,
kuid praktikas võib binaarne otsing olla siiski kiirem, kuna iga samm nõuab väiksemat arvu võrdlusi.



Binary Search tõhusus:

Binary Search on tavaliselt tõhusam, sest:
Teeb vähem võrdlusi. Binary teeb ühe võrdluse iteratsiooni kohta, Ternary Search teeb kaks.
Jaotab kiiremini. Binary Search jagab massiivi pooleks, mis on efektiivsem.
Sellel on madalam üldkulu. Isegi kui O(log⁡3n) tundub parem, on Binary Search'i O(log⁡2n) praktikas kiirem.
Binaarne otsing on tõhusam, kui otsitakse kindlat väärtust järjestatud andmehulgas või kui otsinguväli on suur ja täpsus ei ole äärmiselt oluline, samas kui ternaarsed otsingud on optimeerimisülesannete lahendamiseks.
