class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        count = n
        parent = list(range(n))
        size = [1] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    ri, rj = find(i), find(j)
                    if ri == rj:
                        continue
                    if size[ri] > size[rj]:
                        parent[rj] = ri
                        size[ri] += size[rj]
                    else:
                        parent[ri] = rj
                        size[rj] += size[ri]
                    count -= 1
        return count