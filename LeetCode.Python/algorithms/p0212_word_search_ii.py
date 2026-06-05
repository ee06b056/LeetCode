class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = {}
        find = []
        for w in words:
            node = root
            for c in w:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["#"] = w
        m = len(board)
        n = len(board[0])
        directs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = [[0] * n for _ in range(m)]
        def dfsHelper(r: int, c: int, node: dict) -> None:
            visited[r][c] = 1
            char = board[r][c]
            if char in node:
                if "#" in node[char]:
                    find.append(node[char]["#"])
                    del node[char]["#"]
                for dr, dc in directs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and visited[nr][nc] == 0:
                        dfsHelper(nr, nc, node[char])
                if not node[char]:
                    del node[char]
            visited[r][c] = 0
        for i in range(m):
            for j in range(n):
                dfsHelper(i, j, root)
        return find
