class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 1 (Slow): Time: O(n^2)
        # slow = 0
        # fast = 1

        # while slow < len(nums)-1:
        #     fast = slow + 1
        #     while fast < len(nums):
        #         if nums[slow] + nums[fast] == target:
        #             return [slow, fast]
        #         fast += 1
        #     slow += 1

        # Solution 2 (HashMap):
        #valueAndIndex = {k:v for k, v in zip(nums, range(len(nums)))}
        valueAndIndex = {}
        
        for n, i in zip(nums, range(len(nums))):
            difference = target - n
            if difference in valueAndIndex:
                return [valueAndIndex[difference], i]
            valueAndIndex[n] = i 