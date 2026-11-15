class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time:
        # Space:

        # dp[i]: Fewest # of coins to make up i
        dp = [float('Inf')] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount + 1):
            for coin in coins:
                if coin <= amt:   
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])
        
        return dp[-1] if dp[-1] != float('Inf') else -1

