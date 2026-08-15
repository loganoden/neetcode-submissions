class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Assuming there is exactly one answer
        # Two pointer method works best

        nums_sorted = sorted(nums)

        left = 0
        right = len(nums_sorted) - 1

        while left < right:
            sum = nums_sorted[left] + nums_sorted[right]
            if sum == target:
                return [left, right]
            elif sum < target:
                left += 1
            else:
                right -= 1
