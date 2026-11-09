class Solution:
    def numDecodings(self, s: str) -> int:
        # Time:
        # Space:

        # dp[i] = # of ways to decode the first i digits
        dp = [0] * (len(s) + 1)
        # One way to decode nothing: choose no letters
        dp[0] = 1

        for i in range(1, len(s) + 1):
            # Use the last digit as one letter
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]

            # Use last two digits as one letter
            if i >= 2 and 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]

