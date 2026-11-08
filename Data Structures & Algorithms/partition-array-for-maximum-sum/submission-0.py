class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        # dp[i] max sum of 0 to i-1 elements of arr
        dp = [0] * (len(arr) + 1)

        for start in range(len(arr)):
            max_group_len = min(k, len(arr) - start)
            for end in range(start + 1, start + max_group_len + 1):
                current = arr[end - 1]

                dp[end] = max(dp[end], dp[start] + current * (end - start))

        return dp[-1]
