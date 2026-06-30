class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                ch = heights[stack.pop()]
                cl = i if not stack else i - 1 - stack[-1]
                largest = max(largest, ch * cl)
            stack.append(i)
        return largest