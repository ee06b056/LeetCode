from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        sum_count_dict = defaultdict(int)
        prefix_sum = 0
        count = 0
        sum_count_dict[0] = 1
        for n in nums:
            prefix_sum += n
            target = prefix_sum - k
            count += sum_count_dict[target]
            sum_count_dict[prefix_sum] += 1
        return count
