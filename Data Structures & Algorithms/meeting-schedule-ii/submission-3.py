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
        
        # Use min heap bc we always need the smallest value, so O(1) retrieval
        heapq.heapify(current_ends)

        for i in range(1, len(intervals)):
            # If a room has emptied, then we don't need a new one
            if intervals[i].start >= current_ends[0]:
                heapq.heappop(current_ends)
           
            heapq.heappush(current_ends, intervals[i].end)   

        return len(current_ends)