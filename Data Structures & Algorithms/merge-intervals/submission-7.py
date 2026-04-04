class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = []
        inital = intervals[0]
        for x, y in intervals[1:]:
            if(inital[0] <= x <= inital[1]):
                inital[0] = min(inital[0], x)
                inital[1] = max(inital[1], y)
            else:
                ret.append(inital)
                inital = [x,y]
        
        ret.append(inital)
        return ret
