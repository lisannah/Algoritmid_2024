Ülesanne 3: Jump Search 

Jump search ülevaade ja põhiprintsiibid:

Jump Search - otsingu algoritm sorteeritud massiivide jaoks, mis töötab hüppeliselt. Selle asemel, et kontrollida iga elementi järjest, 
liigub algoritm läbi massiivi kindlate sammudega, tavaliselt suurusega nn​, kus nn on massiivi suurus.
1. Algoritm hüppab elementide vahel kindla intervalliga, kuni leiab vahemiku, kus otsitav väärtus võiks asuda.
2. Seejärel kasutab algoritm Linear Search-i selles vahemikus.
   


Jump Searchi pseudo-kood:

Algus
Määran n kui järjestuse pikkus
Määran step = √n (sammude suurus, mille järgi liigelda)
Leian sobiva ploki, kus element võib olla
Määran prev = 0 (alguspunkt)
Kui arr[min(step, n) - 1] < otsitav väärtus x, siis
Määran prev = step
Määran step = step + √n
Kui prev >= n, siis
Tagasta -1 (elementi ei leitud)
Teen lineaarnse otsingu plokis
Alustan indeksilt prev ja liigun kuni min(step, n) - 1
Kui arr[i] == x, siis
Tagasta i (element leiti)
Kui elementit ei leitud
Tagasta -1 (elementit ei leitud)



Ajaline komplekssus ja kus võib Jump search parem olla kui Linear ja Binary

Jump Search: O(√n) – sobib suurtele sorteeritud järjestustele, kuid on aeglasem kui Binary Search.
Linear Search: O(n) – kõige aeglasem, sobib väikesemahuliste või mittesorteeritud järjestuste jaoks.
Binary Search: O(log n) – kõige kiirem sorteeritud järjestustes, kuna iga samm jagab järjestuse pooleks.
Jump Search on efektiivne siis, kui järjestus on suur ja sorteeritud, kuid ei ole piisavalt suur Binary Searchi kasutamiseks. 
Sobib hästi, kui otsing toimub suurte, kuid mitte liiga suurte andmete puhul.
