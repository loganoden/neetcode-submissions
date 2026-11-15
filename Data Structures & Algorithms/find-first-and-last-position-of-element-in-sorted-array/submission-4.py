class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Time: O(log(n))
        # Space: O(1)
        
        def find_boundary(is_first):
            boundary = -1

            left, right = 0, len(nums) - 1

            while left <= right:
                midpoint = (left + right) // 2

                if nums[midpoint] < target:
                    left = midpoint + 1
                elif nums[midpoint] > target:
                    right = midpoint - 1
                else:
                    if is_first:
                        # Found possible answer
                        boundary = midpoint
                        # Look for earlier one
                        right = midpoint - 1
                    else:
                        # Found possible answer
                        boundary = midpoint
                        # Look for later one
                        left = midpoint + 1
            return boundary

        return [find_boundary(True), find_boundary(False)]