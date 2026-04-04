class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()
        ret = []
        for x,y in intervals:
            if(x <= newInterval[0] <= y or newInterval[0] <= x <= newInterval[1]):
                newInterval[0] = min(newInterval[0], x)
                newInterval[1] = max(newInterval[1], y)
            elif(y < newInterval[0]):
                ret.append([x,y])
            else:
                ret.append(newInterval)
                newInterval = [x,y]
        ret.append(newInterval)
        return ret