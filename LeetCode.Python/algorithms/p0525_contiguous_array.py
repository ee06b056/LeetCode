class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        sum_index_dict = {}
        max_l = 0
        prefix_sum = 0
        sum_index_dict[0] = -1
        for i, n in enumerate(nums):
            prefix_sum += 1 if n == 1 else -1
            if prefix_sum in sum_index_dict:
                max_l = max(max_l, i - sum_index_dict[prefix_sum])
            else:
                sum_index_dict[prefix_sum] = i
        return max_l
    