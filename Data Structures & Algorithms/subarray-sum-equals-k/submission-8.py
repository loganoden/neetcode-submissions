class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Time: O(n), where n = len(nums)
        # Space: O(n)

        # Sum, Freq
        # One empty prefix has sum 0, before nums starts
        seen = {0: 1}

        current_prefix = 0
        total = 0

        for num in nums:
            current_prefix += num
            needed = current_prefix - k
            total += seen.get(needed, 0)

            seen[current_prefix] = seen.get(current_prefix, 0) + 1
        
        return total