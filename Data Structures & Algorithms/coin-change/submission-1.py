class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time: O(A * C), where A = amount and C = len(coins)
        # Space: O(A)

        dp = [float('Inf')] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount + 1):
            for coin in coins:
                if coin <= amt:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])
            
        return dp[-1] if dp[-1] != float('Inf') else -1
            