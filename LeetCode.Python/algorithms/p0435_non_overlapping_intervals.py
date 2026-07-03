class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        current_end = float("-inf")
        intervals.sort(key=lambda x: x[1])
        count = 0
        for i in intervals:
            if i[0] >= current_end:
                current_end = i[1]
            else:
                count += 1
        return count