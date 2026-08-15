"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Sort by start time
        intervals.sort(key=lambda x: x.start)
        req_rooms = 1   

        # Create data structure containing end times of meetings currently occupying rooms
        current_ends = [intervals[0].end]

        for i in range(1, len(intervals)):
            # If a room has emptied, then we don't need a new one
            if intervals[i].start > min(current_ends):
                currents_ends = [x for x in current_ends if x > intervals[i].start]
            # Otherwise, we need a new room
            else:
                req_rooms += 1
            current_ends.append(intervals[i].end)   

        return req_rooms