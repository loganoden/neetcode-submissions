class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_largest = []

        for n in nums:
            if len(k_largest) < k:
                heapq.heappush(k_largest, n)
            elif n > k_largest[0]:
                heapq.heapreplace(k_largest, n)
        
        return k_largest[0]