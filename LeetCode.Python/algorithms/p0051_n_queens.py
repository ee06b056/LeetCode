class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        column = [True] * n
        main_d = [True] * (n * 2 - 1)
        anti_d = [True] * (n * 2 - 1)
        board = [["."] * n for _ in range(n)]
        answer = []
        def dfs(r: int) -> None:
            if r == n:
                temp_b = ["".join(row) for row in board]
                answer.append(temp_b)
                return
            for l in range(n):
                if column[l] and main_d[r - l + n - 1] and anti_d[r + l]:
                    board[r][l] = "Q"
                    column[l] = False
                    main_d[r - l + n - 1] = False
                    anti_d[r + l] = False
                    dfs(r + 1)
                    board[r][l] = "."
                    column[l] = True
                    main_d[r - l + n - 1] = True
                    anti_d[r + l] = True
        dfs(0)
        return answer
