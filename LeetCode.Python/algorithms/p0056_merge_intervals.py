class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x[0])
        answer = []
        ci = intervals[0]
        for interval in intervals:
            if interval[0] > ci[1]:
                answer.append(ci)
                ci = interval
            else:
                ci[1] = max(ci[1], interval[1])
        if ci:
            answer.append(ci)
        return answer