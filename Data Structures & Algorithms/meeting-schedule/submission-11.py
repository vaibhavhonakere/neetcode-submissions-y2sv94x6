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
        inital = intervals[0]

        for pt in intervals[1:]:
            start = pt.start
            end = pt.end
            if(start < inital.end):
                return False
            else:
                inital = pt
        
        return True