class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        myset = set(nums)
        res = 1

        for num in nums:
            x = num-1
            if x not in myset:
                y = num + 1
                while y in myset:
                    res = max(res, y-x)
                    y+=1

        return res

