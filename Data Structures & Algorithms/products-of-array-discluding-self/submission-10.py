class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(1)

        output = [0] * len(nums)

        current = 1
        for i in range(len(nums)):
            output[i] = current
            current *= nums[i]

        current = 1
        for i in reversed(range(len(nums))):
            output[i] *= current
            current *= nums[i]

        return output