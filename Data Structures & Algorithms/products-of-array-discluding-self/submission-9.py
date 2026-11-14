class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(n)

        output = []

        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        current = 1
        for i in range(len(nums)):
            current *= nums[i]
            prefix[i] = current

        current = 1
        for i in reversed(range(len(nums))):
            current *= nums[i]
            postfix[i] = current

        for i in range(len(nums)):
            if i == 0:
                output.append(postfix[i+1])
            elif i == (len(nums) - 1):
                output.append(prefix[i-1])
            else:
                output.append(prefix[i-1] * postfix[i+1])

        return output

