class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            num = matrix[i][j]
            if num == target:
                return True
            elif num < target:
                i += 1
            else:
                j -= 1
        return False