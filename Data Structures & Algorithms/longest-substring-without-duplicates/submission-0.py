class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute force: Start at every character
        # Keep extending right until duplicate
        longest = 0

        for i in range(len(s)):
            seen = set()
            length = 0
            for c in s[i:]:
                if c not in seen:
                    seen.add(c)
                    length += 1
                else:
                    longest = max(length, longest)
                    break

        return longest