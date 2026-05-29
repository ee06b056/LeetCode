from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        island_count = 0
        directs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for i, row in enumerate(grid):
            for j, p in enumerate(row):
                if p == "1":
                    island_count += 1
                    dq = deque()
                    dq.append((i, j))
                    grid[i][j] = "0"
                    while dq:
                        r, c = dq.popleft()
                        for dr, dc in directs:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                                dq.append((nr, nc))
                                grid[nr][nc] = "0"
        return island_count
