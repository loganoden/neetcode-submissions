class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Solution 1 (My Solution) - Time: 0(n^2), Space: 0(n)
        # for i in range(0, len(nums)+1):
        #     if i not in nums:
        #         return i

        # Solution 2 (XOR) - Time: 0(n), Space: 0(1)

        res = 0
        for i in range(1, len(nums)+1):
            res ^= nums[i-1] ^ i
        return res