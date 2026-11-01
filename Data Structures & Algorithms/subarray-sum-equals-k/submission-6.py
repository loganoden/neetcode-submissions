class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Time: O(n), where n = len(nums)
        # Space: O(n)

        # Sum, Freq
        # One empty prefix has sum 0, before nums starts
        seen = {0: 1}

        # Create prefix sum
        prefix = [0] * (len(nums))
        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]

        total = 0

        for current_prefix in prefix:
            needed = current_prefix - k
            total += seen.get(needed, 0)

            seen[current_prefix] = seen.get(current_prefix, 0) + 1
        
        return total
