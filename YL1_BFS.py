
from collections import deque

def laius_otsing(graaf, algus):
    külastatud = set()  # jälgime külastatud sõlmi
    järjekord = deque([algus])  # kasutame järjekorda sõlmede hoidmiseks
    külastatud.add(algus)

    while järjekord:
        sõlm = järjekord.popleft()
        print(sõlm, end=" ")

        # läbime kõik naabersõlmed
        for naaber in graaf[sõlm]:
            if naaber not in külastatud:
                järjekord.append(naaber)
                külastatud.add(naaber)

# graafi esitamine sõnastiku kujul
graaf = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# käivitame BFS algoritmi algussõlmest 'A'
laius_otsing(graaf, 'A')
