import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter_map = Counter(nums)
        h = []
        for n, f in counter_map.items():
            if len(h) < k:
                heapq.heappush(h, (f, n))
            else:
                heapq.heappushpop(h, (f, n))
        return [v for _, v in h]