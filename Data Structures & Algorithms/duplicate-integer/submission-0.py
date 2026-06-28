class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        m = {}
        for num in nums:
            if num in m:
                return True
            m[num] = m.get(num, 0) +1

        return False
        
            
