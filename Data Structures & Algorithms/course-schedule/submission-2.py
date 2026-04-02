from collections import deque
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def has_cycle(start, graph, visited, rec_stack):
            if rec_stack[start]:
                return True

            if visited[start]:
                return False

            visited[start] = True
            rec_stack[start] = True

            for node in graph[start]:
                if has_cycle(node, graph, visited, rec_stack):
                    return True

            rec_stack[start] = False
            return False

        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        visited, rec_stack = [False] * numCourses, [False] * numCourses
        for key in range(numCourses):
            if has_cycle(key, graph, visited, rec_stack):
                return False
        return True


