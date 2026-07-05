class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        n = len(edges)

        vis = [0] * (n+1)
        cycle = set()
        cyclestart = -1

        def dfs(node, parent):
            nonlocal cyclestart
            if vis[node] ==1:
                cyclestart = node
                return True

            vis[node] = 1

            for adj in graph[node]:
                 
                if adj == parent:
                    continue
                if dfs(adj, node):
                    if cyclestart != -1:
                        cycle.add(node)
                    if node == cyclestart:
                        cyclestart = -1
                    return True

            return False

        dfs(1, -1)

        for u, v in reversed(edges):
            if  u in cycle and v in cycle:
                return [u, v]

        return []

        