class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Num, Count
        occurences = {}

        for n in nums:
            occurences[n] = occurences.get(n, 0) + 1

        # Maintain min heap of size K
        min_heap = []

        for num, count in occurences.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                # Evict the lowest frequency item
                heapq.heappop(min_heap)
            
        return [num for count, num in min_heap]
