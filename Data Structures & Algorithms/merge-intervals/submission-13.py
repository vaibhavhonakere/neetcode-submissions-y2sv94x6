class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = [intervals[0]]
        for x,y in intervals:
            if(merged_intervals[-1][1] < x):
                merged_intervals.append([x,y])
            else:
                merged_intervals[-1][0] = min(merged_intervals[-1][0], x)
                merged_intervals[-1][1] = max(merged_intervals[-1][1], y)
        
        return merged_intervals