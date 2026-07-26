class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        a = 0
        for num in nums:
            a = a ^ num
        return a

    def singleNumber_set(self, nums: list[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber_set2(self, nums: list[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        return s.pop()