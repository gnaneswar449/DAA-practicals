import time
from collections import deque

# Predefined graph (adjacency list) - NO user input required
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}


def dfs_traversal(graph, start):
    """Returns the Depth First Search traversal order using an explicit stack."""
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            # Push neighbors in reverse so we visit them in the same order
            # as they appear in the adjacency list.
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order


def bfs_traversal(graph, start):
    """Returns the Breadth First Search traversal order using a queue."""
    visited = set()
    queue = deque([start])
    order = []

    visited.add(start)
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def main():
    start_node = 'A'
    print("DFS and BFS Traversals on a Predefined Graph")
    print("---------------------------------------------")
    print(f"Graph (adjacency list): {graph}")
    print(f"Start node: {start_node}\n")

    # DFS
    dfs_start = time.perf_counter()
    dfs_order = dfs_traversal(graph, start_node)
    dfs_end = time.perf_counter()

    # BFS
    bfs_start = time.perf_counter()
    bfs_order = bfs_traversal(graph, start_node)
    bfs_end = time.perf_counter()

    print("DFS Traversal:", " -> ".join(dfs_order))
    print("BFS Traversal:", " -> ".join(bfs_order))

    print("\n--- Time Complexity ---")
    print("DFS: O(V + E)  (V = number of vertices, E = number of edges)")
    print("BFS: O(V + E)  (V = number of vertices, E = number of edges)")

    print("\n--- Space Complexity ---")
    print("DFS: O(V) worst case (visited set + stack)")
    print("BFS: O(V) worst case (visited set + queue)")

    print(f"\nDFS Execution Time: {dfs_end - dfs_start:.9f} seconds")
    print(f"BFS Execution Time: {bfs_end - bfs_start:.9f} seconds")


if __name__ == "__main__":
    main()