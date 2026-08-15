"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
            
        # Sort intervals based on starting interval value
        intervals.sort(key=lambda x: x.start)

        prev = intervals[0]

        for i in range(1, len(intervals)):
            prev = intervals[i-1]
            if intervals[i].start <= prev.end:
                return False
        
        return True