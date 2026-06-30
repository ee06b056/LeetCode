class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        next_g_dict = {}
        for n in reversed(nums2):
            while stack and stack[-1] <= n:
                stack.pop()
            next_g_dict[n] = -1 if not stack else stack[-1]
            stack.append(n)
        answer = []
        for n in nums1:
            answer.append(next_g_dict[n])
        return answer