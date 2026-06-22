from itertools import accumulate

class NumArray:

    def __init__(self, nums: list[int]):
        self._prefix_sum = []
        sum = 0
        for n in nums:
            sum += n
            self._prefix_sum.append(sum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self._prefix_sum[right]
        else:
            return self._prefix_sum[right] - self._prefix_sum[left - 1]
        
    
class NumArray:

    def __init__(self, nums: list[int]):
        self._prefix = list(accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix[right + 1] - self._prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)