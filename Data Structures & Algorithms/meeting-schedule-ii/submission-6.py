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

        # Process meetings in chronological start order
        # Runtime: O(nlogn)
        intervals.sort(key=lambda x: x.start)

        # End times of rooms currently being used
        # Use min heap bc we always need the smallest value, so O(1) retrieval
        current_ends = [intervals[0].end]

        # Heap can hold up to n end times if every meeting overlaps -> Memory: O(n)
       
        # heappop & heappush -> both O(logn)
        # Across n meetings, so O(nlogn)
        for i in range(1, len(intervals)):
            # Earliest room is free, so reuse it
            if intervals[i].start >= current_ends[0]:
                heapq.heappop(current_ends)
           
            # Current meeting now occupies a room
            heapq.heappush(current_ends, intervals[i].end)   

        return len(current_ends)