from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tail = []
        for n in nums:
            pos = bisect_left(tail, n)
            if pos == len(tail):
                tail.append(n)
            else:
                tail[pos] = n
        return len(tail)

    def lengthOfLIS_dp(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0