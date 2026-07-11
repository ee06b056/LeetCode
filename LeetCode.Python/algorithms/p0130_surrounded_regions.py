from collections import deque

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        dq = deque()
        for i in range(m):
            if board[i][0] == "O":
                board[i][0] = "A"
                dq.append((i, 0))
            if board[i][n - 1] == "O":
                board[i][n - 1] = "A"
                dq.append((i, n - 1))
        for i in range(1, n - 1):
            if board[0][i] == "O":
                board[0][i] = "A"
                dq.append((0, i))
            if board[m - 1][i] == "O":
                board[m - 1][i] = "A"
                dq.append((m - 1, i))
        while dq:
            r, l = dq.popleft()
            for dr, dl in directions:
                nr, nl = r + dr, l + dl
                if 0 <= nr < m and 0 <= nl < n and board[nr][nl] == "O":
                    board[nr][nl] = "A"
                    dq.append((nr, nl))
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"
