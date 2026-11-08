class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # Time: O(n * min(k, n))
        # Space: O(n)
        
        # dp[i]: The best sum for the first i elements (0 to i-1)
        dp = [0] * (len(arr) + 1)

        for start in range(len(arr)):
            max_group_len = min(k, len(arr) - start)

            group_max = 0
            for end in range(start + 1, start + max_group_len + 1):
                group_max = max(group_max, arr[end - 1])
                dp[end] = max(dp[end], dp[start] + group_max * (end - start))

        return dp[-1]
