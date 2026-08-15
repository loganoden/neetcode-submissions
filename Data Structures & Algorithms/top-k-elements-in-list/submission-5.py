class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n) time and O(n) space

        # Create a hash map to store number and frequency
        freq = {}
        elements = []
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Create buckets where index means frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        # Fill buckets
        for num, count in freq.items():
            buckets[count].append(num)

        result = []

        # Traverse buckets from highest frequency to lowest
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

        return result