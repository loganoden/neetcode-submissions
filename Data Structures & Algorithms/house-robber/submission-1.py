class Solution:
    def rob(self, nums: List[int]) -> int:
        two_back = 0
        one_back = 0

        for money in nums:
            current = max(one_back, two_back + money)

            two_back = one_back
            one_back = current

        return one_back