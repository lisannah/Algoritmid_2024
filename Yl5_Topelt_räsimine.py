class ProductCatalog:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Tabel, kus hoiame tooteid

    # Esimene räsi funktsioon (modulaarne)
    def hash1(self, product_id):
        return product_id % self.size

    # Teine räsi funktsioon (väldib kokkupõrkeid)
    def hash2(self, product_id):
        return 1 + (product_id % (self.size - 1))

    # Toote lisamine topelt räsimisega
    def insert(self, product_id, product_info):
        index = self.hash1(product_id)
        step = self.hash2(product_id)

        # Kui koht on juba hõivatud, liigu edasi vastavalt teisest räsimisest saadud sammu suurusele
        while self.table[index] is not None:
            index = (index + step) % self.size

        self.table[index] = (product_id, product_info)

    # Toote otsimine topelt räsimisega
    def search(self, product_id):
        index = self.hash1(product_id)
        step = self.hash2(product_id)

        # Otsime, kuni leiame vastava toote või tühja koha
        while self.table[index] is not None:
            if self.table[index][0] == product_id:
                return self.table[index][1]  # Tagastame toote info
            index = (index + step) % self.size

        return None  # Kui toode ei leita

    # Kogu tabeli kuvamine
    def display(self):
        print("Product Catalog:")
        for i in range(self.size):
            if self.table[i] is None:
                print(f"Index {i}: Empty")
            else:
                product_id, product_info = self.table[i]
                print(f"Index {i}: Product ID {product_id} -> {product_info}")

# Testimine
product_catalog = ProductCatalog(11)  # Loome tootekataloogi hash tabeli suurusega 11

# Lisame tooteid kataloogi
product_catalog.insert(101, {"name": "Laptop", "price": 999.99})
product_catalog.insert(202, {"name": "Smartphone", "price": 499.99})
product_catalog.insert(303, {"name": "Headphones", "price": 79.99})
product_catalog.insert(404, {"name": "Smart Watch", "price": 199.99})
product_catalog.insert(505, {"name": "Keyboard", "price": 49.99})

# Kuvame kogu tootekataloogi
product_catalog.display()

# Otsimine
product_info = product_catalog.search(202)
if product_info:
    print(f"Product found: {product_info}")
else:
    print("Product not found.")

product_info = product_catalog.search(505)
if product_info:
    print(f"Product found: {product_info}")
else:
    print("Product not found.")

product_info = product_catalog.search(999)  # Toode, mida ei ole tabelis
if product_info:
    print(f"Product found: {product_info}")
else:
    print("Product not found.")
    
   
# 1. Kuidas see kood aitab ületada ühekordse räsimise piiranguid?
 
# Topelt räsimine ületab ühekordse räsimise piirangud, kasutades kahte räsimisfunktsiooni.
# Kui tekib kokkupõrge, liigutakse järgmisesse asukohta vastavalt teise funktsiooni väärtusele,
# vältides järjestikuseid kokkupõrkeid, nagu ühekordse räsimise puhul.


# 2. Aja- ja ruumikomplekssus

# Aja keerukus:
# Sisestamine: Parimal juhul (kui ei esine kokkupõrkeid) on aeg O(1).
# Kokkupõrgete korral (kui mitu sammu on vajalik) võib aeg ulatuda O(n), kus n on tabeli suurus.
# Otsimine: Otsimine on samuti keskmiselt O(1), kuid kokkupõrgete korral võib see ulatuda O(n).

# Ruumi keerukus:
# Tabeli suurus on O(n), kus n on tabeli suurus,
# kuna iga toode (võti ja väärtus) on salvestatud tabelis.


# 3. Stsenaarium, kus topelt räsimine on efektiivne

# Topelt räsimine oleks eriti efektiivne suurte andmekogumite puhul,
# kus võtmed on laiali ja kokkupõrked võivad sageli tekkida.
# Näiteks suurte tootekataloogide haldamine e-kaubanduses,
# kus iga toode on ainulaadne ja sisestatakse sageli ja autentimisvõtmed.
