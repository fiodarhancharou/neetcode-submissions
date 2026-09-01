"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        i = 0
        result = []
        while i < len(intervals):
            if result and result[-1].end > intervals[i].start:
                return False
            else:
                result.append(intervals[i])
            i += 1
        return True
            