class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_largest = []

        for n in nums:
            if len(k_largest) >= k:
                if n > k_largest[0]:
                    heapq.heappop(k_largest)
                    heapq.heappush(k_largest, n)
            else:
                heapq.heappush(k_largest, n)
        
        return k_largest[0]