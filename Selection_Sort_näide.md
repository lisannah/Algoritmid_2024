
Algne list=[29,15,56,77,18]

Algus
N = 5 (listi pikkus)
I = 0
MinIndex = 0
List = [29, 15, 56, 77, 18]


Iteratsioon 1 (I = 0)
Sea J = I + 1 = 1
Võrdle List[J] (15) ja List[MinIndex] (29)
MinIndex = 1
Suurenda J (J+1) = 2
Võrdle List[J] (56) ja List[MinIndex] (15)
MinIndex ei muutu.
Suurenda J (J+1) = 3
Võrdle List[J] (77) ja List[MinIndex] (15)
MinIndex ei muutu.
Suurenda J (J+1) = 4
Võrdle List[J] (18) ja List[MinIndex] (15)
MinIndex ei muutu.
Suurenda J (J+1) = 5 (J ei ole enam < N)
Vaheta List[I] (29) ja List[MinIndex] (15)
List pärast vahetust: [15,29,56,77,18][15,29,56,77,18]
Leitud väikseim element: 15


Iteratsioon 2 (I = 1)
Sea MinIndex = I = 1
Sea J = I + 1 = 2
Võrdle List[J] (56) ja List[MinIndex] (29)
MinIndex ei muutu.
Suurenda J (J+1) = 3
Võrdle List[J] (77) ja List[MinIndex] (29)
MinIndex ei muutu.
Suurenda J (J+1) = 4
Võrdle List[J] (18) ja List[MinIndex] (29)
MinIndex = 4
Suurenda J (J+1) = 5 (J ei ole enam < N)
Vaheta List[I] (29) ja List[MinIndex] (18)
List pärast vahetust: [15,18,56,77,29][15,18,56,77,29]
Leitud väikseim element: 18


Iteratsioon 3 (I = 2)
Sea MinIndex = I = 2
Sea J = I + 1 = 3
Võrdle List[J] (77) ja List[MinIndex] (56)
MinIndex ei muutu.
Suurenda J (J+1) = 4
Võrdle List[J] (29) ja List[MinIndex] (56)
MinIndex = 4
Suurenda J (J+1) = 5 (J ei ole enam < N)
Vaheta List[I] (56) ja List[MinIndex] (29)
List pärast vahetust: [15,18,29,77,56][15,18,29,77,56]
Leitud väikseim element: 29


Iteratsioon 4 (I = 3)
Sea MinIndex = I = 3
Sea J = I + 1 = 4
Võrdle List[J] (56) ja List[MinIndex] (77)
MinIndex = 4
Suurenda J (J+1) = 5 (J ei ole enam < N)
Vaheta List[I] (77) ja List[MinIndex] (56)
List pärast vahetust: [15,18,29,56,77][15,18,29,56,77]
Leitud väikseim element: 56


Iteratsioon  5 (I = 4)
Sea MinIndex = I = 4
Ei ole enam elemente, mida võrrelda, kuna J oleks 5.
Vahetust ei ole vaja, kuna see on viimane element.'

Lõplik sorteeritud list  [15,18,29,56,77]
