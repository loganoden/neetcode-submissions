from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Time: 
        # Space:

        words = set(wordDict)
        
        # Returns true if we can split everything from start onward into dict words
        @cache
        def can_split(start):
            if start == len(s):
                return True

            for i in range(start + 1, len(s) + 1):
                if s[start:i] in words:
                    if can_split(i):
                        return True
            return False

        return can_split(0)
            
