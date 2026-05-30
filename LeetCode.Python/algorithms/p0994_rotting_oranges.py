from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        minutes = 0
        fresh = 0
        dq = deque()
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    fresh += 1
                elif cell == 2:
                    dq.append((i, j))
        directs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        m = len(grid)
        n = len(grid[0])
        while dq and fresh:
            for _ in range(len(dq)):
                r, c = dq.popleft()
                for dr, dc in directs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        dq.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            minutes += 1
        return -1 if fresh > 0 else minutes
