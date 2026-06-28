class Solution:
    def recursion(self, nums , res, i, currlist, currsum, target):
        if currsum == target:
            res.append(currlist.copy())
            return 

        if i>= len(nums) or currsum> target:
            return

        currlist.append(nums[i])
        self.recursion(nums, res, i, currlist, currsum + nums[i] , target)
        currlist.pop()

        self.recursion(nums, res, i+1, currlist, currsum, target)




    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        self.recursion(nums, res, 0, [], 0 , target)

        return res