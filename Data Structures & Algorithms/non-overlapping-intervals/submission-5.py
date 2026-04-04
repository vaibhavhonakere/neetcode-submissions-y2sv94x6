class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        count = 0
        for s,e in intervals[1:]:
            if(prevEnd <= s):
                prevEnd = e
            else:
                count += 1
                prevEnd = min(prevEnd, e)
        return count