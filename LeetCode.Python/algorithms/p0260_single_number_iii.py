class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        ns = set()
        for num in nums:
            if num in ns:
                ns.remove(num)
            else:
                ns.add(num)
        return list(ns)

    def singleNumber_xor(self, nums: list[int]) -> list[int]:
        xor = 0
        for num in nums:
            xor ^= num

        # Find the rightmost set bit
        diff = xor & -xor

        a = 0
        b = 0
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num

        return [a, b]