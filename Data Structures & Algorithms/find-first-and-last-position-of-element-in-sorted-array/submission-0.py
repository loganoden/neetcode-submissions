class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Time: O(log(n))
        # Space: O(1)
        
        first, last = -1, 1

        # Find first occurence
        left, right = 0, len(nums) - 1

        while left <= right:
            midpoint = (left + right) // 2

            if nums[midpoint] < target:
                left = midpoint + 1
            elif nums[midpoint] > target:
                right = midpoint - 1
            else:
                # Found possible answer
                first = midpoint
                # Look for earlier one
                right = midpoint - 1

        # Reset to search entire array again
        left, right = 0, len(nums) - 1

        while left <= right:
            midpoint = (left + right) // 2

            if nums[midpoint] < target:
                left = midpoint + 1
            elif nums[midpoint] > target:
                right = midpoint - 1
            else:
                # Found possible answer
                last = midpoint
                # Look for later one
                left = midpoint + 1

            return [first, last]


