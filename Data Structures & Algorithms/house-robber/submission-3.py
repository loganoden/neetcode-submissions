class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)

        # Best total through previous house
        one_back = 0

        # Best total through two houses ago
        two_back = 0

        for money in nums:
            # Either rob this house or skip it
            current = max(money + two_back, one_back)

            two_back = one_back
            one_back = current

        return one_back