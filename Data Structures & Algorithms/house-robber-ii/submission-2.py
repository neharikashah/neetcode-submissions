class Solution:
    def robb(self, start, end, nums):

        take = 0
        skip = 0

        for i in range(start, end+1):
            newtake = skip + nums[i]
            newskip = max(skip, take)

            take = newtake
            skip = newskip


        return max(take, skip)


    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        return max(self.robb(0, n-2, nums), self.robb(1, n-1, nums))

