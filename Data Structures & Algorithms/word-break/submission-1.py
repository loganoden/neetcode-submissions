class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Time:
        # Space:

        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for start in range(len(s)):
            if not dp[start]:
                continue
            for end in range(start + 1, len(s) + 1):   
                if s[start:end] in words:
                    dp[end] = True

        return dp[-1]
        