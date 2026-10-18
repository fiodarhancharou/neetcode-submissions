"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        size = len(intervals)
        intervals.sort(key=lambda x: x.start)
        rooms = []
        for i in intervals:
            if rooms and rooms[0] <= i.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, i.end)
        return len(rooms)
        