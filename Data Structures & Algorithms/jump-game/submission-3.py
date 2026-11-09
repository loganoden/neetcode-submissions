class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Time: O(n)
        # Space: O(1)

        farthest = 0
        for i, jump in enumerate(nums):
            if i > farthest:
                return False

            farthest = max(farthest, i + jump)
        
        return True