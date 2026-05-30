from collections import defaultdict

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