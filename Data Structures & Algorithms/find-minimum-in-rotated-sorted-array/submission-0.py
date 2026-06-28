class Solution:
    def findMin(self, a: List[int]) -> int:
        n = len(a)

        l = 0
        r = n-1

        while l < r:
            mid = int((l+r)/2)
            if a[mid] > a[r]: #pivot at right 
                l = mid+1
            elif a[mid] < a[l]: #pivot at left
                r = mid
            else: #normal binary search
                if a[mid] < a[r]:
                    r = mid -1
                else:
                    l = mid
                    
        return a[l]

