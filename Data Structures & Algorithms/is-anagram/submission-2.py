class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 4 (Best, Time: O(s + t), Space: O(1))
        if len(s) != len(t):
            return False

        count = [0] * 26
        for a, b in zip(s, t):
            count[ord(a) - ord('a')] += 1
            count[ord(b) - ord('a')] -= 1

        return all(x == 0 for x in count)
        
        # Solution 1 (Time: O(s + t), Space: O(s + t)); -> s + t can also be n if you assume len(s) == len(t)
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

        # Solution 2 (Time: O(s + t), Space: O(s + t))
        return Counter(s) == Counter(t)

        # Solution 3 (Time: O(nlogn), Space: O(1) -> Interviewers assume sorting doesn't take extra memory, but Python's is actually O(n))
        return sorted(s) == sorted(t)

       