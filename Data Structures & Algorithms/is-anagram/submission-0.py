class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for c in s:
            if c in t:
                i = t.index(c)
                t = t[:i] + t[i+1:]
            else:
                return False
        return True