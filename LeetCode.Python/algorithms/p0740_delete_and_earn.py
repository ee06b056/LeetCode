from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        max_number = 0
        counter = {}
        for num in nums:
            max_number = max(max_number, num)
            if num in counter:
                counter[num] += num
            else:
                counter[num] = num
        a, b = 0, 0
        for i in range(1, max_number + 1):
            a, b = b, max(b, a + counter.get(i, 0))
        return b

    def deleteAndEarn_dp(self, nums: list[int]) -> int:
        nums_counter = Counter(nums)
        nums_list = []
        for k, v in nums_counter.items():
            nums_list.append((k, v * k))
        nums_list.sort(key=lambda x: x[0])
        a, b = 0, 0
        for i in range(len(nums_list)):
            if i > 0 and nums_list[i][0] == nums_list[i - 1][0] + 1:
                a, b = b, max(b, a + nums_list[i][1])
            else:
                a, b = b, b + nums_list[i][1]
        return b