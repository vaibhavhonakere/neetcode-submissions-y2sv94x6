class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        for s, e in intervals:
            if(s <= newInterval[0] and newInterval[0] <= e) or (newInterval[0] <= s and s <= newInterval[1]):
                newInterval[0], newInterval[1] = min(s, newInterval[0]), max(e, newInterval[1])
                # res.append([min(s, newInterval[0]), min(e, newInterval[1])])
            elif(s <= newInterval[0] and e <= newInterval[0]):
                res.append([s,e])
            else:
                #print([newInterval[0], newInterval[1]])
                res.append([newInterval[0], newInterval[1]])
                newInterval[0], newInterval[1] = s,e
        res.append(newInterval)
        return res
            