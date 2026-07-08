class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_v = nums[mid]
            left_v = nums[left]
            if mid_v == target:
                return mid
            elif target == left_v:
                return left
            if mid_v > left_v:
                if mid_v > target > left_v:
                    right = mid - 1
                else:
                    left = mid + 1
            elif mid_v < left_v:
                if left_v > target > mid_v:
                    left = mid + 1
                else:
                    right = mid - 1 
            else:
                left = mid + 1
        return -1