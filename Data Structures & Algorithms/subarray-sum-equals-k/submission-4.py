class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Hash Table + Prefix Sum
        total_count = 0
        current_sum = 0

        # Prefix Sum: Occurences
        prefix = {0: 1}

        for num in nums:
            current_sum += num

            # current_sum - needed = k
            needed = current_sum - k

            if needed in prefix:
                total_count += prefix[needed]
            
            prefix[current_sum] = prefix.get(current_sum, 0) + 1

        return total_count