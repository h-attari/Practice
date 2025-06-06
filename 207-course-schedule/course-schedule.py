
class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Build adjacency list
        graph = defaultdict(list)
        for pair in prerequisites:
            course, prerequisite = pair
            graph[course].append(prerequisite)

        # Check if there is a cycle
        visited = [0] * numCourses  # 0 - not visited, 1 - visiting, 2 - visited

        def hasCycle(course):
            if visited[course] == 1:
                return True
            if visited[course] == 2:
                return False

            visited[course] = 1
            for prerequisite in graph[course]:
                if hasCycle(prerequisite):
                    return True

            visited[course] = 2
            return False

        # Perform DFS for each course
        for course in range(numCourses):
            if hasCycle(course):
                return False

        return True