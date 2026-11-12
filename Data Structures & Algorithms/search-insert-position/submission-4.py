class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Time: O(n)
        # Space: O(1)

        left, right = 0, len(nums) - 1
        while left <= right:
            midpoint = (left + right) // 2               
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                right = midpoint - 1
            elif nums[midpoint] < target:
                left = midpoint + 1

        return left