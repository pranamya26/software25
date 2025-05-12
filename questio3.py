# BFS TRAVERSAL
import collections

def bfs(graph, root):
    visited = set()
    queue = collections.deque([root])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            for i in graph[vertex]:  # FIXED: iterate over neighbors
                if i not in visited:  # FIXED: corrected syntax
                    queue.append(i)

    print(visited)

if __name__ == "__main__":  # FIXED: corrected syntax
    # Dictionary
    graph = {
        0: [1, 2, 3],
        1: [0, 2],
        2: [0, 1, 4],
        3: [0],
        4: [2]
    }
    bfs(graph, 0)

# DFS TRAVERSAL (Iterative using Stack)
def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=" ")  # Process the node
            visited.add(vertex)
            # Add neighbors to stack (reversed for correct DFS order)
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
dfs(graph,0)