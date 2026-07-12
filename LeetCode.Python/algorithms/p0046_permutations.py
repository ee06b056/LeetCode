class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        l = len(nums)
        used = set()
        permutation = []
        answer = []
        def dfs() -> None:
            if len(permutation) == l:
                answer.append(permutation[:])
                return
            for i in range(l):
                if i not in used:
                    permutation.append(nums[i])
                    used.add(i)
                    dfs()
                    permutation.pop()
                    used.remove(i)
        dfs()
        return answer