Ülesanne 5: Stabiilsus ja adaptiivsus sortimisel 


a) Defineeri, mida tähendab, et sortimisalgoritm on "stabiilne." Anna näide stabiilsest sortimisalgoritmist antud loendist.

Stabiilne sortimisalgoritm säilitab sama väärtusega elementide algse järjekorra ka pärast sortimist.  
Näiteks, kui loendis on kaks 3 väärtust, kus esimene asub enne teist, jääb see järjekord samaks ka pärast sortimist.
Insertion Sort on stabiilne.



b) Selgita "adaptiivsuse" kontseptsiooni sortimisel. Millistest eelmainitud sortimisalgoritmidest peetakse adaptiivseks?

Adaptiivne sortimisalgoritm saab osaliselt sorteeritud loendi kiiremini järjestada,
kohandades tööd vastavalt sellele, kui sorteeritud loend juba on. Mida rohkem on loend algselt sorteeritud, seda vähem samme on vaja.
Insertion Sort ja Bubble Sort on adaptiivsed, kuna nad suudavad tuvastada osaliselt sorteeritud loendid ja vajavad sellisel juhul vähem tööd.
Selection Sort ei ole adaptiivne, sest see võtab igal juhul sama arvu samme, sõltumata sellest, kui palju loend on eelnevalt järjestatud.
