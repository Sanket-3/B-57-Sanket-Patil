graph = {
    'A': {'B':1, 'C':3},
    'B': {'D':3, 'E':1},
    'C': {'F':5},
    'D': {},
    'E': {'F':1},
    'F': {}
    }

heuristic = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 6,
    'E': 1,
    'F': 0
    }

open_list = ['A']
closed_list = []

g = {'A': 0}

while open_list:
    node = min(open_list, key=lambda x:g[x] + heuristic[x])
    print(node, end=" ")
    
    if node == 'F':
        break
    
    open_list.remove(node)
    closed_list.append(node)
    
    for neigbor in graph[node]:
        cost = g[node] + graph[node][neigbor]
        
        if neigbor not in open_list and neigbor not in closed_list:
            open_list.append(neigbor)
            g[neigbor] = cost