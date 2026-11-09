class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Time:
        # Space:

        farthest = 0
        
        for i, jump in enumerate(nums):
            if i > farthest:
                return False

            farthest = max(farthest, i + jump)
        
        return True if farthest == len(nums) - 1 else False