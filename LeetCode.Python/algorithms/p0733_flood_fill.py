from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: return image
        originalcolor = image[sr][sc]
        m = len(image)
        n = len(image[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        visited[sr][sc] = 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dequeue = deque()
        dequeue.append((sr, sc))
        while len(dequeue) > 0:
            r, c = dequeue.popleft()
            image[r][c] = color
            for d in directions:
                nextr = r + d[0]
                nextc = c + d[1]
                if 0 <= nextr < m and 0 <= nextc < n and visited[nextr][nextc] == 0 and image[nextr][nextc] == originalcolor:
                    dequeue.append((nextr, nextc))
                    visited[nextr][nextc] = 1
        return image
    
    def floodFillBeter(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc] == color:
            return image
        originalcolor = image[sr][sc]
        m = len(image)
        n = len(image[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        q.append((sr, sc))
        while q:
            r, c = q.popleft()
            image[r][c] = color
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == originalcolor:
                    q.append((nr, nc))
        return image


# Variant — marks the image on enqueue rather than on dequeue. This is what
# the "drop the visited matrix" idea actually requires to work: once a cell is
# flipped to `color`, the neighbor predicate `image[nr][nc] == original_color`
# alone is enough to prevent re-enqueueing. Marking on dequeue (as in
# `floodFillBeter` above) leaves a window where the same cell can be enqueued
# by multiple neighbors before it's first popped.
class Solution2:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image
        m, n = len(image), len(image[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        image[sr][sc] = color
        q = deque([(sr, sc)])
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == original_color:
                    image[nr][nc] = color
                    q.append((nr, nc))
        return image