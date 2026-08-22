class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window
        seen = set()

        left = 0
        longest = 0

        for right in range(len(s)):
            # Move left ptr forward while right is a dup
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            longest = max(longest, right - left + 1)

        return longest