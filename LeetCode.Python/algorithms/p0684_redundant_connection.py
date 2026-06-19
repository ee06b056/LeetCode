class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        size = [1] * (n + 1)
        parents = list(range(n + 1))

        def find(x: int) -> int:
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x
        
        for edge in edges:
            x, y = edge
            rx, ry = find(x), find(y)
            if rx == ry:
                return edge
            if size[rx] > size[ry]:
                parents[ry] = rx
                size[rx] += size[ry]
            else:
                parents[rx] = ry
                size[ry] += size[rx]
        
        return []
