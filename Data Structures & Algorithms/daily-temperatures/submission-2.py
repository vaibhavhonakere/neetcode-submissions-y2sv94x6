class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonic_decreasing_stack = [] # [index, value]
        daily_temps = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):
            index = i
            while(monotonic_decreasing_stack and monotonic_decreasing_stack[-1][1] < temp):
                index, _ = monotonic_decreasing_stack.pop()
                daily_temps[index] = i - index
            monotonic_decreasing_stack.append([i, temp])
        
        return daily_temps

