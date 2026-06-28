class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        l = 0
        r = 0
        maxl = 1
        start = 0

        for i in range(n):
            l = i
            r = i

            while l>=0 and r<n and s[l] == s[r]:
                if  r-l+1 > maxl:
                    maxl =  r-l+1
                    start = l
                

                l-=1
                r+=1
            

        for i in range(n):
            l = i
            r = i+1

            while l>=0 and r<n and s[l] == s[r]:
                if  r-l+1 > maxl:
                    maxl =  r-l+1
                    start = l

                l-=1
                r+=1

        return s[start: start+maxl]
        
        
