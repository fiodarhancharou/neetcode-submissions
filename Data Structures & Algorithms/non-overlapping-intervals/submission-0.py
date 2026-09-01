class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        i = 0
        result = []
        while i<len(intervals):
            if not result or intervals[i][0] >= result[-1][1]:
                result.append(intervals[i])
            i += 1
        return len(intervals) - len(result)