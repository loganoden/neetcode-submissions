class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Put all values into a set
        # If the set length is less than the list length,
        # return false. Otherwise, return true

        return len(set(nums)) < len(nums)
