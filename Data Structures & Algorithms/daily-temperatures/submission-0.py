class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(n)

        # Stack to hold all temps still waiting for warmer day
        stack = []
        waiting_times = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                current = stack.pop()
                waiting_times[current] = i - current

            stack.append(i)

        return waiting_times