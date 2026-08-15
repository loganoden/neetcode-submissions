class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute force: Start at every character
        # Keep extending right until duplicate
        longest = 0

        for i in range(len(s)):
            seen = set()

            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                
                seen.add(s[j])
                longest = max(longest, j - i + 1)

        return longest