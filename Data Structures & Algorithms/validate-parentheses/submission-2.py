class Solution:
    def isValid(self, s: str) -> bool:
        # Maintain a stack to hold all open brackets
        # If open bracket is found, add to stack
        # If closed bracket is found, check top entry of stack
        # If matching bracket type, then pop

        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for bracket in s:
            # If open bracket, then append to stack
            if bracket not in pairs:
                stack.append(bracket)

            # Closing bracket must match most recent opening bracket
            elif not stack or stack[-1] != pairs[bracket]:
                return False

            # Otherwise, pop from stack
            else:
                stack.pop()

        # If there are no remaining front brackets, return true
        return not stack

