class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Assuming nums is sorted
        # Assuming there is exactly one answer
        # Two pointer method works best

        left = 0
        right = len(nums) - 1

        inverted_list = False
        # Swap behavior if list is inverted
        if nums[left] > nums[right]: 
            inverted_list = True

        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return [left, right]
            elif sum < target:
               # inverted: right decr by 1, left incr by 0
               # not inverted: right decr by 0, left incr by 1
                right -= int(inverted_list)
                left += int(not inverted_list)
            else:
               # inverted: right decr by 0, left incr by 1
               # not inverted: right decr by 1, left incr by 0
                right -= int(not inverted_list)
                left += int(inverted_list)
