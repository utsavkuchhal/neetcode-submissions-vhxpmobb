from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        queue = deque()
        for index, val in enumerate(indegree):
            if val == 0:
                queue.append(index)
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return result if len(result) == numCourses else []