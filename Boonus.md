BOONUS

Kuidas näeks loend [8, 3, 5, 4, 7, 6, 2] välja pärast esimest läbimist antud algoritmide puhul
a) Bubble Sort
b) Selection Sort
c) Insertion Sort

Bubble Sort: [3, 5, 4, 7, 6, 2, 8]
Selection Sort: [2, 3, 5, 4, 7, 6, 8]
Insertion Sort: [3, 8, 5, 4, 7, 6, 2]

Sest:

a) Bubble Sort
[8, 3, 5, 4, 7, 6, 2] – 8 ja 3 vahetatakse -> [3, 8, 5, 4, 7, 6, 2]
[3, 8, 5, 4, 7, 6, 2] – 8 ja 5 vahetatakse -> [3, 5, 8, 4, 7, 6, 2]
[3, 5, 8, 4, 7, 6, 2] – 8 ja 4 vahetatakse -> [3, 5, 4, 8, 7, 6, 2]
[3, 5, 4, 8, 7, 6, 2] – 8 ja 7 vahetatakse -> [3, 5, 4, 7, 8, 6, 2]
[3, 5, 4, 7, 8, 6, 2] – 8 ja 6 vahetatakse -> [3, 5, 4, 7, 6, 8, 2]
[3, 5, 4, 7, 6, 8, 2] – 8 ja 2 vahetatakse -> [3, 5, 4, 7, 6, 2, 8]
Tulemus pärast esimest läbimist: [3, 5, 4, 7, 6, 2, 8]

b) Selection Sort
Algne loend: [8, 3, 5, 4, 7, 6, 2]
Väikseim element on 2.
Vahetame 2 ja 8 kohad.
Tulemus pärast esimest läbimist: [2, 3, 5, 4, 7, 6, 8]

c) Insertion Sort
Algne loend: [8, 3, 5, 4, 7, 6, 2]
Võrdleme 3 ja 8: 3 on väiksem, seega paigutame 3 enne 8.
Tulemus pärast esimest läbimist: [3, 8, 5, 4, 7, 6, 2]
