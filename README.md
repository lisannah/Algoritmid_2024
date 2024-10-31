
Insertion Sort'i sammud

Algne loend: [12, 11, 13, 5, 6, 7]

1. Iteratsioon (töötame elemendi 11 kallal):
Võrdleme 11 ja 12: 11 < 12, seega nihutame 12 paremale.
Uus loend: [12, 12, 13, 5, 6, 7]
Sisestame 11: loend muutub: [11, 12, 13, 5, 6, 7]


2. Iteratsioon (töötame elemendi 13 kallal):
13 on juba õiges kohas, loend jääb: [11, 12, 13, 5, 6, 7]
   
3. Iteratsioon (töötame elemendi 5 kallal):
Nihutame 13, 12 ja 11 paremale, et lisada 5:
Loend muutub: [11, 11, 12, 13, 6, 7] (ajutine)
Sisestame 5: loend muutub: [5, 11, 12, 13, 6, 7]

4. Iteratsioon (töötame elemendi 6 kallal):
Nihutame 13, 12 ja 11 paremale, et lisada 6:
Loend muutub: [5, 11, 11, 12, 13, 7] (ajutine)
Sisestame 6: loend muutub: [5, 6, 11, 12, 13, 7]


5. Iteratsioon (töötame elemendi 7 kallal):
Nihutame 13, 12 ja 11 paremale, et lisada 7:
Loend muutub: [5, 6, 11, 11, 12, 13] (ajutine)
Sisestame 7: loend muutub: [5, 6, 7, 11, 12, 13]
Lõplik loend on: [5, 6, 7, 11, 12, 13]

Insertion Sort on tõhusam osaliselt sorteeritud loendi puhul,
kuna see nõuab vähem võrdlusi ja nihutusi. Osaliselt sorteeritud loendi korral 
on paljud elemendid juba õigetes positsioonides,
mistõttu algoritm suudab kiiresti leida õiged kohad uutele elementidele.
