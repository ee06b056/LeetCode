from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m = len(heights)
        n = len(heights[0])
        directs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        p_set: set[tuple[int, int]] = set()
        a_set: set[tuple[int, int]] = set()
        p_set.update((0, j) for j in range(n))
        p_set.update((i, 0) for i in range(m))
        a_set.update((m - 1, j) for j in range(n))
        a_set.update((i, n - 1) for i in range(m))
        def bfs(reachable: set[tuple[int, int]]) -> None:
            dq = deque(reachable)
            while dq:
                i, j = dq.popleft()
                for di, dj in directs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in reachable and heights[ni][nj] >= heights[i][j]:
                        dq.append((ni, nj))
                        reachable.add((ni, nj))
        bfs(p_set)
        bfs(a_set)
        return [list(cell) for cell in p_set & a_set]
