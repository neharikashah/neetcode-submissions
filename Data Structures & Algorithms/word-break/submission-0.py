class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [0] * (n+1)

        dp[0] = 1

        for i in range(1, n+1):
            for w in words:
                st = i - len(w)

                if st>=0 and dp[st] == 1 and s[st:i] == w:
                    dp[i] = 1
                    break

        if dp[-1] == 1:
            return True
        return False