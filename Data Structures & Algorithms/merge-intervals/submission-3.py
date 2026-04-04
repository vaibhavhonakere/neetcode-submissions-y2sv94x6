class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        first = intervals[0]
        res = []

        for s, e in intervals[1:]:
            if(first[0] <= s <= first[1]):
                first[0] = min(first[0], s)
                first[1] = max(first[1], e)
            else:
                res.append([first[0], first[1]])
                first[0] = s
                first[1] = e
        
        res.append([first[0], first[1]])
        return res
