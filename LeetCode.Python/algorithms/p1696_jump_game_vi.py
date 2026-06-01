from collections import deque

class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        dq = deque()
        pre_sum = nums[0]
        for i in range(1, len(nums)):
            while dq and dq[-1][1] <= pre_sum:
                dq.pop()
            dq.append((i - 1, pre_sum))
            if dq[0][0] < i - k:
                dq.popleft()
            pre_sum = nums[i] + dq[0][1]
        return pre_sum
