class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Use binary search

        left, right = 0, len(nums)
        while left < right:
            midpoint = (left + right) // 2               
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                right = midpoint - 1
            elif nums[midpoint] < target:
                left = midpoint + 1

        return left