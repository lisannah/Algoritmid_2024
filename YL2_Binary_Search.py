# Binary Search algoritm

def binary_search(arr, target):
    vasak = 0
    parem = len(arr) - 1

    while vasak <= parem:
        keskel = vasak + (parem - vasak) // 2
        
        # Kontrollime, kas element keskel on sihtmärk
        if arr[keskel] == target:
            return keskel  # Tagastame indeks, kus sihtmärk asub
        elif arr[keskel] < target:
            vasak = keskel + 1  # Otsime paremat pooli
        else:
            parem = keskel - 1  # Otsime vasakut pooli

    return -1  # Kui sihtmärk ei ole massiivis, tagastame -1

# Testimine
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} leiti indeksil {result}.")
else:
    print(f"Element {target} ei ole massiivis.")

# 2. Võrreldes Binary Search ja Linear Search aegkomplekse:
# - Binary Search aegkompleksus on O(log n), kuna igal sammul vähendatakse otsinguala poole võrra.
# - Linear Search aegkompleksus on O(n), kuna iga element tuleb järjest läbi vaadata.

# 3. Näide, kus Binary Search on kasulikum kui Linear Search:
# Kui massiiv on sorteeritud ja väga suur (nt miljoneid elemente), siis Binary Search töötab palju kiiremini, 
# kuna iga samm väheneb poole võrra. Linear Search peab kontrollima kõiki elemente järjest, mis võib olla väga aeglane.
