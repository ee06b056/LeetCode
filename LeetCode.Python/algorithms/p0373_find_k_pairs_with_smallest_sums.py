import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        h = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, len(nums1)))]
        heapq.heapify(h)
        k_smallest_pairs = []
        for i in range(k):
            if not h:
                break
            _, m, n = heapq.heappop(h)
            k_smallest_pairs.append([nums1[m], nums2[n]])
            if n < len(nums2) - 1:
                heapq.heappush(h, (nums1[m] + nums2[n + 1], m, n+ 1))
        return k_smallest_pairs