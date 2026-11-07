from collections import defaultdict
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Let V = numCourses and E = len(prequisites)
        # Time: O(V + E)
        # Space: O(V + E)

        adj = defaultdict(list)
        indeg = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indeg[course] += 1

        queue = deque()

        for course, num_prereq in enumerate(indeg):
            if num_prereq == 0:
                queue.append(course)

        completed = 0

        while queue:
            prereq = queue.popleft()
            completed += 1

            for course in adj[prereq]:
                indeg[course] -= 1
                if indeg[course] == 0:
                    queue.append(course)

        return completed == numCourses
                
