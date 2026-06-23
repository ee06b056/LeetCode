class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            sum = max(sum, window_sum)
        return sum / k