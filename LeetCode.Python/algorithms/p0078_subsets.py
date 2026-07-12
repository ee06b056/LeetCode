class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        answer = [[]]
        subset = []
        n = len(nums)
        def dfs(index: int) -> None:
            if index == n:
                return
            for i in range(index, n):
                subset.append(nums[i])
                answer.append(subset[:])
                dfs(i + 1)
                subset.pop()
        dfs(0)
        return answer
    
    def subsets_iterative(self, nums: list[int]) -> list[list[int]]:
        answer = [[]]
        for num in nums:
            answer += [curr + [num] for curr in answer]
        return answer
    
    def subsets_bitmask(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        answer = []
        for i in range(1 << n):
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(nums[j])
            answer.append(subset)
        return answer