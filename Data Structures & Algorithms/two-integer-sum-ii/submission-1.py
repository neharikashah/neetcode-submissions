class Solution:
    def twoSum(self, a: List[int], t: int) -> List[int]:
        n = len(a)

        l = 0 
        r = n-1

        while l<r:
            if a[l] + a[r] == t:
                return [l+1, r+1]
            elif a[l] + a[r] > t:
                r-=1
            else:
                l+=1

        return [-1, -1]

