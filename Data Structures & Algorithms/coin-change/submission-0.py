class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount +1] * (amount + 1)

        n = len(coins)
        dp[0] = 0

        for i in range(n):
            for j in range(1, amount + 1):
                if j >= coins[i]:
                    dp[j] = min(dp[j], dp[j - coins[i]]+1)
        
        if dp[amount] > amount:
            return -1
        else:
            return dp[amount]

        