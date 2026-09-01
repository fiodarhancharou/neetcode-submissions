from queue import Queue


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = {n: [] for n in range(n)}
        meetings.sort(key=lambda x: x[0], reverse=True)
        while meetings:
            event = meetings.pop()            
            room = 0
            earliest_start = float("inf")
            for key in rooms:
                if not rooms[key] or rooms[key][-1][1] <= event[0]:
                    room = key
                    earliest_start = event[0]
                    break
                else:
                    if rooms[key][-1][1] < earliest_start:
                        room = key
                        earliest_start = rooms[key][-1][1]
            late_time = earliest_start - event[0]
            event[0] += late_time
            event[1] += late_time
            rooms[room].append(event)
        result = [(len(rooms[key]), key) for key in rooms]
        result.sort(key=lambda x: x[0])
        max_val = result[-1][0]
        all_equal = [i[1] for i in result if i[0]==max_val]
        return min(all_equal)