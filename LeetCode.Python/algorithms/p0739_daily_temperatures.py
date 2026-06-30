class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        answer = []
        for i in reversed(range(len(temperatures))):
            t = temperatures[i]
            while stack and stack[-1][1] <= t:
                stack.pop()
            answer.append(0 if not stack else stack[-1][0] - i)
            stack.append((i, t))
        answer.reverse()
        return list(answer)
    
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                d = stack.pop()
                answer[d] = i - d
            stack.append(i)
        return answer