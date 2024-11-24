class Node:
    #Sõlme klass üheühenduselisele seotud listile.
    def __init__(self, key, value):
        self.key = key  # Võti
        self.value = value  # Väärtus
        self.next = None  # Järgmine sõlm
 
class HashTable:
    #Hash-tabel, mis kasutab separate chainingut seotud listidega.
    def __init__(self, size):
        self.size = size  # Hash-tabeli suurus
        self.table = [None] * self.size  # Initsialiseerime tabeli tühjade väärtustega
 
    def _hash_function(self, key):
        #ihtne hash-funktsioon."""
        return hash(key) % self.size
 
    def insert(self, key, value):
        #Lisab hash-tabelisse uue võtme ja väärtuse paari.
        index = self._hash_function(key)
        node = self.table[index]
        # Kui indeksis pole veel sõlme, loome uue
        if node is None:
            self.table[index] = Node(key, value)
            return
        # Liigume seotud listis, et kontrollida, kas võti juba eksisteerib
        prev = None
        while node is not None:
            if node.key == key:
                # Võti juba eksisteerib, uuendame väärtust
                node.value = value
                return
            prev = node
            node = node.next
        # Võtit ei leitud, lisame uue sõlme listi lõppu
        prev.next = Node(key, value)
 
    def search(self, key):
        #Otsib hash-tabelist võtit ja tagastab selle väärtuse.
        index = self._hash_function(key)
        node = self.table[index]
        while node is not None:
            if node.key == key:
                return node.value  # Võti leitud
            node = node.next
        return None  # Võtit ei leitud
 
    def delete(self, key):
        #Kustutab hash-tabelist võtme ja väärtuse paari.
        index = self._hash_function(key)
        node = self.table[index]
        prev = None
        while node is not None:
            if node.key == key:
                # Võti leitud, eemaldame selle
                if prev is None:
                    # Kustutatav sõlm on listi esimene
                    self.table[index] = node.next
                else:
                    # Kustutatav sõlm on keskel või lõpus
                    prev.next = node.next
                return True
            prev = node
            node = node.next
        return False  # Võtit ei leitud
 
    def display(self):
        #Kuvab hash-tabeli sisu."""
        for i in range(self.size):
            print(f"Ämber {i}: ", end='')
            node = self.table[i]
            while node is not None:
                print(f"({node.key}, {node.value}) -> ", end='')
                node = node.next
            print("None")
 
# Näide kasutusest:
if __name__ == "__main__":
    ht = HashTable(10)
    ht.insert("õun", 1)
    ht.insert("banaan", 2)
    ht.insert("apelsin", 3)
    ht.insert("viinamari", 4)
    ht.insert("melon", 5)
 
    ht.display()
 
    print("Otsime 'õun':", ht.search("õun"))
    print("Otsime 'banaan':", ht.search("banaan"))
    print("Otsime 'kirss':", ht.search("kirss"))
 
    ht.delete("banaan")
    ht.display()
    
    
# 2. Separate Chaining vs. Open Addressing: Ajaline ja Ruumiline Komplekssus

# Separate Chaining:
# Ajaline komplekssus: Keskmiselt O(1), kuid halvematel juhtudel (palju kokkupõrkeid) O(n).
# Ruumiline komplekssus: O(n), kuna iga lahter sisaldab linked-listi.
# Open Addressing:
# Ajaline komplekssus: Keskmiselt O(1), kuid ülekoormatud tabelis O(n).
# Ruumiline komplekssus: O(n), kuna kõik andmed salvestatakse tabeli lahtritesse.



# 3. Separate Chaining eelised ja puudused

# Eelised: +
# + Lihtne rakendada.
# + Ei sõltu tabeli koormusest, sest iga kokkupõrge lahendatakse eraldi linked-listis.
# 
# Puudused: - 
# - Lisab täiendavat ruumi linked-listide jaoks.
# - Tabel võib muutuda ebaefektiivseks, kui palju elemente satuvad ühte lahtrisse.