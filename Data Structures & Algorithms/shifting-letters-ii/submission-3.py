class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Time: O(n + m), where n = len(s), m = len(shifts)
        # Space: O(n)
        
        diff = [0] * (len(s) + 1)
        result = []
        min_ord = ord('a')

        for start, end, direction in shifts:
            # +1 for going forward, -1 for going backward
            shift = direction * 2 - 1

            diff[start] += shift
            diff[end + 1] -= shift

        running = 0
        for i, c in enumerate(s):
            running += diff[i]

            alphabet_index = (ord(c) - min_ord + running) % 26
            result.append(chr(min_ord + alphabet_index))

        return "".join(result)