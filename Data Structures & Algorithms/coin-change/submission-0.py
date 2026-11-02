class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Save previously discovered min num of coins
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a:
                    # Use coin plus the best answer for what's left
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return dp[amount] if dp[amount] != float("inf") else -1
