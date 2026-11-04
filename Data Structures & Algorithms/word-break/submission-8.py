from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Time: O(n * L^2), where L is the longest dictionary word's length
        # Space: O(n + w), where w is the number of dictionary words

        words = set(wordDict)
        max_word_len = max(len(word) for word in wordDict)
        
        # Returns true if we can split everything from start onward into dict words
        @cache
        def can_split(start):
            if start == len(s):
                return True

            longest_possible_word = min(max_word_len, len(s) - start)
            for i in range(start + 1, start + longest_possible_word + 1):
                if s[start:i] in words:
                    if can_split(i):
                        return True
            return False

        return can_split(0)