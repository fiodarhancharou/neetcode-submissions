"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sweep = []
        for i in intervals:
            sweep.append((i.start, 1))
            sweep.append((i.end, -1))
        sweep.sort(key=lambda x: (x[0], x[1]))
        max_rooms = 0
        cur_rooms = 0
        for _, delta in sweep:
            cur_rooms += delta
            max_rooms = max(max_rooms, cur_rooms)
        return max_rooms