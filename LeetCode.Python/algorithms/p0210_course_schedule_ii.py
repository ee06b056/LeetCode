from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_dict = defaultdict(list)
        indegree = [0] * numCourses
        course_order = []
        for course, pre in prerequisites:
            adj_dict[pre].append(course)
            indegree[course] += 1
        dq = deque(course for course, course_indegree in enumerate(indegree) if course_indegree == 0)
        while dq:
            course = dq.popleft()
            course_order.append(course)
            for next_course in adj_dict[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    dq.append(next_course)
        return course_order if all(c_in == 0 for c_in in indegree) else []
