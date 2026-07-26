class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()

    def hammingWeight_loop(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

    def hammingWeight_kernighan(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count