class Solution:
    def rob(self, nums: List[int]) -> int:
        # Two options, count by even index or count by odd index
        # Compare total profit for both and pick the greatest

        even_profit = 0
        odd_profit = 0

        for i in range(0, len(nums), 2):
            even_profit += nums[i]

        for i in range(1, len(nums), 2):
            odd_profit += nums[i]

        return max(even_profit, odd_profit)
        

