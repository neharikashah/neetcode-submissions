class Solution:
    def maxSubArray(self, num: List[int]) -> int:
        n = len(num)
        if n== 0:
            return n

        currmax = num[0]
        maxsub = num[0]

        for i in range(1, n):
            currmax = max(currmax+num[i], num[i])
            maxsub = max(currmax, maxsub)

        return maxsub
        