class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0 :
            return 0

        take = 0
        skip = 0

        for num in nums:
            newtake = skip + num
            newskip = max(skip, take)

            take = newtake
            skip = newskip


        return max(take, skip)
