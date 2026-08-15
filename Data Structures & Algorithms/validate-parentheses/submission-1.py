class Solution:
    def isValid(self, s: str) -> bool:
        # Maintain a stack to hold all open brackets
        # If open bracket is found, add to stack
        # If closed bracket is found, check front entry of stack
        # If matching bracket type, then pop, otherwise return false

        open_stack = []
        open_closed_pairs = {')': '(', '}': '{', ']': '['}

        for bracket in s:
            # If open bracket, then append to stack
            if bracket in open_closed_pairs.values():
                open_stack.append(bracket)
            else:
                # If open stack is not empty and 
                # if closed bracket's complement is at top of stack
                # then pop top entry of stack
                if open_stack and open_stack[-1] == open_closed_pairs[bracket]:
                    open_stack.pop()
                # Otherwise, ordering is wrong, so return False
                else:
                    return False
        # If there are remaining open brackets, return False, otherwise True
        if open_stack:
            return False
        return True

