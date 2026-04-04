"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        if(len(intervals) > 1): 
            prev = intervals[0]

        for i in range(1, len(intervals)):
            check = intervals[i]
            if prev.end > check.start:
                return False
            prev = check
        return True