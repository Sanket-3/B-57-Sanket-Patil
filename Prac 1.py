graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
    }

#DFS
visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
    
    for i in graph[node]:
        dfs(i)

#BFS
def bfs(start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            
            for i in graph[node]:
                queue.append(i)
                
            
print("DFS Traversal: ")
dfs('A')
print("\nDFS Traversal: ")
bfs('A')

            
