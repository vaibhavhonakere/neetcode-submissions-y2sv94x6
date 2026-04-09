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
                newInterval[0] = min(x, newInterval[0])
                newInterval[1] = max(y, newInterval[1])

        ret.append(newInterval)
        return ret