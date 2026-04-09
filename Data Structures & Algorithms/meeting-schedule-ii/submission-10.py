"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # meetings = [
        #     [1320, 120],   # 22:00 → 00:00
        #     [1380, 120],   # 23:00 → 01:00
        #     [60, 120],     # 01:00 → 03:00
        #     [90, 60]       # 01:30 → 02:30
        # ]

        # custom_intervals = []

        # for start, duration in meetings:
        #     if(start + duration < 1440):
        #         custom_intervals.append([start, start + duration])
        #     else:
        #         custom_intervals.append([start, 1440])
        #         custom_intervals.append([0, (start + duration) % 1440])
            
        # custom_intervals.sort(key=lambda x: x[0])
        # min_heap = []
        # ret = 0

        # for interval in custom_intervals:
        #     while min_heap and min_heap[0] <= interval[0]:
        #         heapq.heappop(min_heap)
        #     heapq.heappush(min_heap, interval[1])
        #     ret = max(len(min_heap), ret)

        # return ret
        # intervals.sort(key=lambda x:x.start)
        start = []
        end = []
        for interval in intervals:
            s = interval.start
            e = interval.end
            start.append(s)
            end.append(e)

        start.sort()
        end.sort()
        
        s = 0
        e = 0
        max_meeting_rooms = 0
        count = 0
        while(s < len(start) and e < len(end)):
            if(start[s] < end[e]):
                s += 1
                count += 1
                # print(s, count)
            else:
                e += 1
                count -= 1
            max_meeting_rooms = max(max_meeting_rooms, count)
        
        return max_meeting_rooms



        