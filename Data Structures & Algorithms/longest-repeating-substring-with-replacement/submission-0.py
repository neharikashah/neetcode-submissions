class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charset = set(s)

        for c in charset:
            l = 0 #left pointer
            count = 0
            for r in range(len(s)): #right pointer
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    #increse the left pointer if window is invalid
                    # also decrease the count before moving l

                    if s[l] == c:
                        count-=1
                    l+=1

                res = max(res, r-l+1) #checking max for every valid window

        return res
