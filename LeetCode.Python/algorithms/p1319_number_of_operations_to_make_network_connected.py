class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        parents = list(range(n))
        size = [1] * n
        count = n

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
                    parents[ry] = rx
                    size[rx] += size[ry]
                else:
                    parents[rx] = ry
                    size[ry] += size[rx]
                count -= 1
        
        for x, y in connections:
            union(x, y)
        return count - 1