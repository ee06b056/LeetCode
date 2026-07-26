class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = []
        for num in range(n + 1):
            ans.append(num.bit_count())
        return ans

    def countBits_dp(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        for num in range(1, n + 1):
            ans[num] = ans[num >> 1] + (num & 1)
        return ans

    def countBits_kernighan(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        for num in range(1, n + 1):
            ans[num] = ans[num & (num - 1)] + 1
        return ans