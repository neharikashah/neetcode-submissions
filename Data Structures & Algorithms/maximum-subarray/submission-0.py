class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0:
            return 0

        currsum = nums[0]
        maxsum = nums[0]

        for i in range(1, n):
            currsum = max(nums[i], nums[i]+ currsum)
            maxsum = max(maxsum, currsum)

        return maxsum
        