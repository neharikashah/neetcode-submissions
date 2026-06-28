class Solution:
    def search(self, a: List[int], t: int) -> int:
        n = len(a)

        l = 0
        r = n-1

        while l <= r:
            mid = int((l+r)/2)
            if a[mid] == t:
                return mid
            elif a[mid] > a[r]: #pivot at right 
                if t>= a[l] and t < a[mid]: 
                    r = mid-1
                else:
                    l = mid +1

            elif a[mid] < a[l]: #pivot at left
                if t> a[mid] and t <= a[r]: 
                    l = mid +1
                else:
                    r = mid -1

            else: #normal binary search
                if a[mid] < t :
                    l = mid +1
                else:
                    r = mid-1
                    
        return -1