Ülesanne 4: Ajakompleksuste analüüs 


a)Millistel eelmainitud sortimisalgoritmidel on halvimal juhul ajakompleksus O(n^2)?
Kõigil kolmel mainitud algoritmil – Bubble Sort, Selection Sort ja Insertion Sort,
sest igaüks neist võrdleb iga elementi teistega vähemalt üks kord, kui loend on täielikult sortimata. 

b) Milline sortimisalgoritm oleks kõige sobivam sortimaks loendit täisarvudega, mis jäävad vahemikku 1 kuni 100 ja miks?
Kõige sobivam algoritm siin oleks Counting Sort, 
kuna see on efektiivne, kui sorteeritavad väärtused on teadaolevas kitsas vahemikus. 
Counting Sort saab kasutada antud vahemiku 1 kuni 100 jaoks loenduritabelit, mis võimaldab seda teha ajakompleksusega O(n + k).
