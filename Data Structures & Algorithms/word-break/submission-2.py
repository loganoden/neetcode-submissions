class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Time: O(n^3) in Python due to substring slicing and hashing
        # Space: O(n + w), where w is the number of dictionary words

        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        max_word_len = max(len(word) for word in wordDict)

        for start in range(len(s)):
            if not dp[start]:
                continue
            longest_possible_word = min(max_word_len, len(s) - start)
            for end in range(start + 1, start + longest_possible_word + 1):   
                if s[start:end] in words:
                    dp[end] = True

        return dp[-1]