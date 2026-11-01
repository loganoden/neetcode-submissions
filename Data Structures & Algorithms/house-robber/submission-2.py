class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)

        # Best total through two houses ago
        two_back = 0
        # Best total through the previous house
        one_back = 0

        for money in nums:
            # Choose to skip this house or rob it and skip its neighbor
            current = max(one_back, two_back + money)

            # Move the saved totals forward for the next house
            two_back = one_back
            one_back = current

        return one_back