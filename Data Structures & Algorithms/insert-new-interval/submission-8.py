class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []

        for i, (x,y) in enumerate(intervals):
            if(y < newInterval[0]):
                ret.append([x,y])
            elif(newInterval[1] < x):
                ret.append(newInterval)
                return ret + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], x)
                newInterval[1] = max(newInterval[1], y)

        ret.append(newInterval)
        return ret