import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h)
        for i in range(k, len(nums)):
            heapq.heappushpop(h, nums[i])
        return heapq.heappop(h)