class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}
        for index, value in enumerate(nums):
            comp = target - value
            if comp in seen:
                return [seen[comp], index]
            seen[value] = index
        return []