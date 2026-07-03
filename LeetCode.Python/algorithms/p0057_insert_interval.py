class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        answer = []
        for i in intervals:
            if newInterval[1] < i[0]:
                answer.append(newInterval)
                newInterval = i
            elif newInterval[0] > i[1]:
                answer.append(i)
            else:
                left = min(i[0], newInterval[0])
                right = max(i[1], newInterval[1])
                newInterval = [left, right]
        answer.append(newInterval)
        return answer