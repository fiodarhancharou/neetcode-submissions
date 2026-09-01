class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        i = 0
        result = 0
        last_end = float("-inf")
        while i<len(intervals):
            if intervals[i][0] < last_end:
                result += 1
            else:
                last_end = intervals[i][1]
            i += 1
        return result