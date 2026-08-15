class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        left = 0
        right = left

        seen = set()

        while left < len(s):
            if right < len(s) and s[right] not in seen:
                seen.add(s[right])
                longest = max(longest, right - left + 1)
                right += 1
            else:
                seen.remove(s[left])
                left += 1
                right = left

        return longest