class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Intervals is a list of lists

        # Sort intervals based on starting value of interval
        list.sort(intervals, key=lambda x: x[0])

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                merged[-1] = [merged[-1][0], intervals[i][1]]
            else:
                merged.append(intervals[i])
        
        return merged