class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Time: O(n + m), where n = len(s) and m = len(shifts)
        # Space: O(n)

        # Extra slot to record a stop at index len(s)
        diff = [0] * (len(s) + 1)

        for start, end, direction in shifts:
            movement = direction * 2 - 1
            diff[start] += movement
            diff[end + 1] -= movement

        min_ord = ord('a')
        running_shift = 0
        result = []

        for i, c in enumerate(s):
            running_shift += diff[i]

            shifted_i = (ord(c) - min_ord + running_shift) % 26
            result.append(chr(min_ord + shifted_i))

        return "".join(result)