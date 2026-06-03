class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def searchHelper(left: int, right: int) -> int:
            if nums[left] > target or nums[right] < target:
                return -1
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            mid = (left + right) // 2
            if nums[mid] < target:
                return searchHelper(mid + 1, right)
            elif nums[mid] > target:
                return searchHelper(left, mid)
            else:
                return mid
        return searchHelper(0, len(nums) - 1)
    
    def searchIterative(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left  = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1
