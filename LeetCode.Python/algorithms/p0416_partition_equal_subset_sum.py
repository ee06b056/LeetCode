class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for n in nums:
            for x in range(target, n - 1, -1):
                if dp[x - n]:
                    dp[x] = True
                    if x == target:
                        return True
        return dp[target]

    def canPartition_set(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = {0}
        for n in nums:
            new_dp = set(dp)
            for x in dp:
                if x + n == target:
                    return True
                if x + n < target:
                    new_dp.add(x + n)
            dp = new_dp
        return False