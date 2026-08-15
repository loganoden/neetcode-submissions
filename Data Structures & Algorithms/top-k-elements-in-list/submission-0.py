class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a heapmap to store number and frequency
        freq = {}
        elements = []
        
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for key, value in freq.items():
            if value == k:
                elements.append(key)

        return elements