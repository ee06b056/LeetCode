class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            hl, hr = height[left], height[right]
            w = right - left
            contains = w * min(hl, hr)
            max_area = max(max_area, contains)
            if hl < hr:
                left += 1
            else:
                right -= 1
        return max_area