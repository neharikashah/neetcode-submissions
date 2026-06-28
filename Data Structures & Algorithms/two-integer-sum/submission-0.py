class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        n = len(nums)
        m = {}
        for i in range(n):
            if t - nums[i] in m:
                return [m[t - nums[i]], i]

            m[nums[i]] = i

        return [0, 0]