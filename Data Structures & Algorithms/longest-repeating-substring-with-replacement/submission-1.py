class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charset = set(s)

        # for c in charset:
        #     l = 0 #left pointer
        #     count = 0
        count = {}
        maxf = 0
        l = 0
        for r in range(len(s)): #right pointer
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                #increse the left pointer if window is invalid
                # also decrease the count before moving l

                count[s[l]] -= 1
                l+=1

            res = max(res, r-l+1) #checking max for every valid window

        return res
