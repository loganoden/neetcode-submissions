class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)

        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            # Try selling today using min prior buy
            price = prices[i]
            profit = price - min_price
            max_profit = max(max_profit, profit)

            # Today's price becomes possible buy for future days
            min_price = min(min_price, price)

        return max_profit
