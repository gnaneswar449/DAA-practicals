# Practical 8: Depth First Search (DFS) and Breadth First Search (BFS) Traversals

This practical demonstrates **graph traversal** using **Depth First Search (DFS)** and **Breadth First Search (BFS)**. The graph is **predefined** in the program, so no user input is required.

---

## Problem Statement

Given a connected, undirected graph represented as an adjacency list, traverse all its vertices starting from a given node using both DFS and BFS, and print the order in which the nodes are visited.

This solution uses an **explicit stack** for DFS and a **queue** for BFS.

---

## Key Idea

- **DFS (Depth First Search)** explores as far as possible along each branch before backtracking. It is implemented iteratively using a **stack** (LIFO).
- **BFS (Breadth First Search)** explores all neighbours of a node before moving to the next level. It is implemented iteratively using a **queue** (FIFO from `collections.deque`).

Both algorithms use a `visited` set to avoid revisiting nodes and prevent infinite loops (important for graphs with cycles).

Predefined graph used:

```
A -- B -- D
|    |
E -- C -- F
```

---

## Time and Space Complexity

| Algorithm | Time Complexity | Space Complexity |
| :--- | :---: | :---: |
| DFS | $O(V + E)$ | $O(V)$ worst case |
| BFS | $O(V + E)$ | $O(V)$ worst case |

Where $V$ = number of vertices and $E$ = number of edges. Each vertex and edge is visited exactly once, hence the $O(V + E)$ time complexity.

---

## Python Program

```python
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

    dfs_start = time.perf_counter()
    dfs_order = dfs_traversal(graph, start_node)
    dfs_end = time.perf_counter()

    bfs_start = time.perf_counter()
    bfs_order = bfs_traversal(graph, start_node)
    bfs_end = time.perf_counter()

    print("DFS Traversal:", " -> ".join(dfs_order))
    print("BFS Traversal:", " -> ".join(bfs_order))

    print("\n--- Time Complexity ---")
    print("DFS: O(V + E)")
    print("BFS: O(V + E)")

    print("\n--- Space Complexity ---")
    print("DFS: O(V) worst case")
    print("BFS: O(V) worst case")

    print(f"\nDFS Execution Time: {dfs_end - dfs_start:.9f} seconds")
    print(f"BFS Execution Time: {bfs_end - bfs_start:.9f} seconds")


if __name__ == "__main__":
    main()
```

---

## Example Output

```text
DFS and BFS Traversals on a Predefined Graph
---------------------------------------------
Graph (adjacency list): {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
Start node: A

DFS Traversal: A -> B -> D -> E -> F -> C
BFS Traversal: A -> B -> C -> D -> E -> F

--- Time Complexity ---
DFS: O(V + E)
BFS: O(V + E)

--- Space Complexity ---
DFS: O(V) worst case
BFS: O(V) worst case

DFS Execution Time: 0.000012500 seconds
BFS Execution Time: 0.000009200 seconds
```

---

## How to Run

```bash
cd practical-08-dfs-bfs
python dfs_bfs.py
```

---

## Author

**Gnaneswar Vuyyuri**