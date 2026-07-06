class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        minHeap = [(0, k)]
        vis = set()
        maxt = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in vis:
                continue
            vis.add(n1)
            maxt = w1

            for n2, w2 in graph[n1]:
                if n2 not in vis:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        if len(vis) == n:
            return maxt
        else:
            return -1



        

        