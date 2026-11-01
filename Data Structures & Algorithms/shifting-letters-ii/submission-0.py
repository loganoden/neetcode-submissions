class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Convert each character to its ordinal standard in ASCII
        min_ord, max_ord = ord('a'), ord('z')

        def wrap_boundaries(current_ord):
           return min_ord + (current_ord - min_ord) % 26
        
        ord_list = [ord(c) for c in s]

        for op in shifts:
            start = op[0]
            end = op[1]
            # Scaled to -1 or 1
            movement = op[2] * 2 - 1

            for i in range(start, end+1):
                ord_list[i] += movement

        string_list = []
        for num in ord_list:
            ordinal = num
            if ordinal < min_ord or ordinal > max_ord:
                ordinal = wrap_boundaries(ordinal)
            string_list.append(chr(ordinal))
           
        return "".join(string_list)
            



