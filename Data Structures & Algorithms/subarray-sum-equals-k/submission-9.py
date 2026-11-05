class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Time:
        # Space:

        # Sum, Frequency
        # An empty prefix has sum 0
        seen = {0: 1}

        current_prefix = 0
        total_count = 0

        for n in nums:
            current_prefix += n
            # current_prefix - needed = k
            needed = current_prefix - k
            total_count += seen.get(needed, 0)

            seen[current_prefix] = seen.get(current_prefix, 0) + 1

        return total_count