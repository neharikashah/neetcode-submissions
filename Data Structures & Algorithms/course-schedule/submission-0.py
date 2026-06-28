class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if there is a cycle return false

        graph = defaultdict(list)

        for first, second in prerequisites:
            graph[second].append(first)

        vis  = [0] * numCourses

        def cycle(i):
            if vis[i] == 1:
                return True
            if vis[i] == 2:
                return False

            vis[i] = 1
            for adj in graph[i]:
                if cycle(adj):
                    return True
            vis[i] = 2

            return False



        for course in range(numCourses):
            if cycle(course):
                return False
        
        return True
