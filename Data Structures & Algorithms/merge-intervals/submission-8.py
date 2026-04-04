class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = [intervals[0]]
        for x,y in intervals[1:]:
            if(ret[-1][0] <= x <= ret[-1][1]):
                ret[-1][0] = min(ret[-1][0], x)
                ret[-1][1] = max(ret[-1][1], y)
            elif(ret[-1][1] < x):
                ret.append([x,y])
        #     else:
        #         ret.append(newInterval)
        #         newInterval = [x,y]
        # ret.append(newInterval)
        return ret