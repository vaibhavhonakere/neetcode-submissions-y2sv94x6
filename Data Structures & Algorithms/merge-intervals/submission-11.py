class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = [intervals[0]]

        for x,y in intervals[1:]:
            if(ret[-1][1] < x):
                ret.append([x,y])
            else:
                ret[-1][0] = min(x, ret[-1][0])
                ret[-1][1] = max(y, ret[-1][1])
        
        return ret