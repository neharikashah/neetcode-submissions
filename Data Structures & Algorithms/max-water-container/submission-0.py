class Solution:
    def maxArea(self, h: List[int]) -> int:
        maxwater = 0
        n = len(h)


        l = 0
        r = n-1

        while l < r:
            minh = min (h[l], h [r])

            maxwater = max(maxwater, minh * (r-l))

            if h[l] < h[r]:
                l+=1
            else:
                r-=1

        return maxwater

        
