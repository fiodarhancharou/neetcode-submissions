class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # insert intervals before
        result = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # insert with possible merges the new interval
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i+=1
        result.append(newInterval)

        # insert intervals after
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        return result
