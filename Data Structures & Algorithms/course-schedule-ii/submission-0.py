class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for x, y in prerequisites:
            graph[y].append(x)

        vis = [0] * numCourses
        res = []

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
            res.append(i)

            

        for i in range(numCourses):
            if cycle(i):
                return []
        
        return res[::-1]
