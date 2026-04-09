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
        if(len(intervals) == 0):
            return True
        prevEnd = intervals[0].end

        for pt in intervals[1:]:
            start = pt.start
            end = pt.end
            if(prevEnd <= start):
                prevEnd = end
            else:
                return False
        
        return True