class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        a, b = nums[0], nums[0]
        for i in range(2, len(nums) - 1):
            a, b = b, max(b, a + nums[i])
        rob_1st = b
        a, b = 0, nums[1]
        for i in range(2, len(nums)):
            a, b = b, max(b, a + nums[i])
        no_rob_1st = b
        return max(rob_1st, no_rob_1st)

    def rob_dp(self, nums: list[int]) -> int:
        def rob_linear(nums: list[int]) -> int:
            a, b = 0, 0
            for num in nums:
                a, b = b, max(b, a + num)
            return b
        if len(nums) == 1:
            return nums[0]
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
