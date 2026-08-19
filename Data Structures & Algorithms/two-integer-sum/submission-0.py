class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        slow = 0
        fast = 1

        while slow < len(nums)-1:
            fast = slow + 1
            while fast < len(nums):
                if nums[slow] + nums[fast] == target:
                    return [slow, fast]
                fast += 1
            slow += 1