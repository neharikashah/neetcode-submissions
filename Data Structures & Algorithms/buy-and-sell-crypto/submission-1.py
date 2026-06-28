class Solution:
    def maxProfit(self, p: List[int]) -> int:
        n = len(p)

        maxp = 0

        i = 0
        minp = 101

        while i < n:
            minp = min(minp, p[i])
            maxp = max(maxp, p[i] - minp)

            i+=1

        return maxp
