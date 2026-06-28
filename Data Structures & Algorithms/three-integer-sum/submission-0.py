class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        i = 0

        while i<n:

            if i > 0 and nums[i] == nums[i - 1]:
                i+=1
                continue

            target = -1 * nums[i]
            temp = []
            
            # while i+1<n and nums[i] == nums[i+1]:
            #     i+= 1

            l = i+1 
            r = n-1

            #binary search 

            while l < r:

                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    l+=1
                    r-=1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1


                elif nums[l] + nums[r] < target:
                    l+=1;

                else:
                    r-=1



            i+=1;
        return res





