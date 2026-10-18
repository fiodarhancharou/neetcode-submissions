"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        size = len(intervals)
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        starts.sort()
        ends.sort()
        max_rooms = 0
        cur_rooms = 0
        s, e = 0, 0
        while s<size and e<size:
            if starts[s] < ends[e]:
                cur_rooms += 1
                s += 1
            else:
                cur_rooms -= 1
                e += 1
            max_rooms = max(max_rooms, cur_rooms)
        
        return max_rooms
        