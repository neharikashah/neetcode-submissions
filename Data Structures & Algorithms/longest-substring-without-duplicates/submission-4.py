class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl = 1
        

        m = {}
        start = -1 
        n = len(s)
        if n == 0:
            return 0
        for i in range(n):                
            if s[i] in m:
                start = max(start,m[s[i]])
            
            m[s[i]] = i
            #start = m[s[i]]

            maxl = max(maxl, i-start)

        return maxl




