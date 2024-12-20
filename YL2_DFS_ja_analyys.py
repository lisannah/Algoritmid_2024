
# graafi esitus 
graaf = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graaf, node, külastatud):
    if node not in külastatud:
        print(node)  # väljasta sõlm
        külastatud.add(node)  # lisa sõlm külastatute hulka
        for naaber in graaf[node]:
            dfs(graaf, naaber, külastatud)

# alguspunkt ja DFS-i käivitamine
alguspunkt = 'A'
külastatud = set()
dfs(graaf, alguspunkt, külastatud)


# Ajakompleksus: O(12), sest O(V+E) = O(6+6) = O(12)
# Ruumikompleksus: O(6), sest O(V) = O(6)
# V = sõlmed
# E = servad
