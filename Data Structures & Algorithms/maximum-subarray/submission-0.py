class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Solution 1: Kadane's Algorithm | Time: O(n)
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(curSum, maxSum)

        return maxSum