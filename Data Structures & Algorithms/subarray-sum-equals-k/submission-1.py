class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Hash Table + Prefix Sum

        # Final output
        output = []

        # Make prefix sum
        pref_sum = {}
        running = 1

        for i, num in enumerate(nums):
            pref_sum[i] = pref_sum.get(i, 0) + running
            running += num
        
        for i, num in enumerate(pref_sum):
            wanted = num - k
            if wanted in pref_sum[i:]:
                output.append([pref_sum.key(wanted), nums[i]])
        
        return output
