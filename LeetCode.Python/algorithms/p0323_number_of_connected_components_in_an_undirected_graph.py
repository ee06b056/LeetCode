class Solution:
    # Three approaches to counting connected components, catalogued together.
    # All three share the name countComponents, so only the LAST def (Approach 3,
    # iterative DFS over an adjacency list) actually binds at runtime — the first
    # two are kept side-by-side for comparison, mirroring program.py's find variants.

    # Approach 1 — Union-Find (DSU): union by size + path-halving find.
    # O(n + e·α(n)) ≈ O(n + e) time, O(n) space. The canonical DSU solution.
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        count = n
        parents = list(range(n))
        size = [1] * n

        def find(x: int) -> int:
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        def union(x: int, y: int) -> None:
            nonlocal count
            rx, ry = find(x), find(y)
            if rx != ry:
                if size[rx] > size[ry]:
                    parents[rx] = ry
                    size[ry] += size[rx]
                else:
                    parents[ry] = rx
                    size[rx] += size[ry]
                count -= 1
        
        for x, y in edges:
            union(x, y)
        return count

    # Approach 2 — recursive DFS over an adjacency MATRIX.
    # O(n²) time and space (building the n×n matrix and scanning each full row
    # dominate, regardless of edge count); recursive, so it risks Python's ~1000
    # recursion limit on a long chain. Correct, but the weakest of the three.
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = [[0] * n for _ in range(n)]
        for x, y in edges:
            graph[x][y] = 1
            graph[y][x] = 1
        visited = [0] * n
        count = 0
        
        def dfs_helper(x: int) -> None:
            for y, c in enumerate(graph[x]):
                if c == 1 and visited[y] == 0:
                    visited[y] = 1
                    dfs_helper(y)
        
        for x in range(n):
            if visited[x] == 0:
                visited[x] = 1
                count += 1
                dfs_helper(x)
        
        return count
    
    # Approach 3 — iterative DFS over an adjacency LIST (this is the one that binds).
    # O(n + e) time and space, no recursion ceiling. Most efficient and robust.
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        visited = [False] * n
        count = 0

        for x in range(n):
            if not visited[x]:
                visited[x] = True
                count += 1
                stack = [x]
                while stack:
                    current = stack.pop()
                    for y in graph[current]:
                        if not visited[y]:
                            visited[y] = True
                            stack.append(y)

        return count
