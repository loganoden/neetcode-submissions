class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        # dp[i] max sum of 0 to i-1 elements of arr
        dp = [0] * (len(arr) + 1)

        for start in range(len(arr)):
            max_group_len = min(k, len(arr) - start)

            group_max = 0
            for end in range(start + 1, start + max_group_len + 1):
                current = arr[end - 1]
                group_max = max(group_max, current)

                dp[end] = max(dp[end], dp[start] + group_max * (end - start))

        return int(dp[-1])
