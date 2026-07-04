class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u) 

        count = 0
        vis = [0] * n

        for i in range(n):
            if vis[i] == 0:
                count +=1
                self.dfs(vis, graph, i)

        return count
    

    def dfs(self, vis, graph, i):
        if vis[i] == 1:
            return 
        vis[i] = 1

        for adj in graph[i]:
            self.dfs(vis, graph, adj)

        
        return
