class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_chars = set()
        longest = 0

        left = 0

        for right in range(len(s)):
            while s[right] in current_chars:
                current_chars.remove(s[left])
                left += 1
            
            current_chars.add(s[right])
            longest = max(longest, len(current_chars))

        return longest