class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums) - 1
        ans = [0] * len(nums)
        i = len(nums) - 1
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                ans[i] = nums[r] ** 2
                r -= 1
            else:
                ans[i] = nums[l] ** 2
                l += 1
            i -= 1
        return ans