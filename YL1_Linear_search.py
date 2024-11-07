def linear_search(arr, target):
    # Läbime kõik elemendid loendis arr
    for i in range(len(arr)):
        # Kui leidub otsitav väärtus, tagastame selle indeksi
        if arr[i] == target:
            return i
    # Kui väärtus pole loendis, tagastame -1
    return -1

# Näide:
arr = [52, 3, 69, 6, 7, 3]
target = 69

result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} leiti indeksil {result}.")
else:
    print(f"Element {target} ei leitud.")
