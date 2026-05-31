from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_dict = defaultdict(list)
        visited_dict = defaultdict(int)
        for c, pre in prerequisites:
            adj_dict[c].append(pre)
        def dfs(course: int) -> bool:
            if visited_dict[course] == 1:
                return False
            if visited_dict[course] == 2:
                return True
            visited_dict[course] = 1
            for pre in adj_dict[course]:
                flag = dfs(pre)
                if not flag:
                    return False
            visited_dict[course] = 2
            return True
        return all(dfs(course) for course in range(numCourses))
    
    def canFinishKahn(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_dict = defaultdict(list)
        indegree = [0] * numCourses
        for c, pre in prerequisites:
            adj_dict[pre].append(c)
            indegree[c] += 1
        dq = deque(i for i, c in enumerate(indegree) if c == 0)
        while dq:
            c = dq.popleft()
            for next_c in adj_dict[c]:
                indegree[next_c] -= 1
                if indegree[next_c] == 0:
                    dq.append(next_c)
        return all(c == 0 for c in indegree)
