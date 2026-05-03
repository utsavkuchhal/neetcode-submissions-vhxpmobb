
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
        # graph -> {1 -> [0, 2], 0 -> [2]}
        def has_cycle(start):
            if stack_visited[start]:
                return True
            
            if visited[start]:
                return False
    
            stack_visited[start] = True
            visited[start] = True
            for r_course in graph[start]:
                if has_cycle(r_course):
                    return True
            stack_visited[start] = False
            result.append(start)
            return False

        result = []
        visited = [False] * numCourses
        stack_visited = [False] * numCourses
        for course in range(numCourses):
            if has_cycle(course):
                return []
        return result[::-1]
            