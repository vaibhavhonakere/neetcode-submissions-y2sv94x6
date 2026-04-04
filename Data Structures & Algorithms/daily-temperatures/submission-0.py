class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0]*len(temperatures)

        stack = [] # (num, index)

        for i, n in enumerate(temperatures):
            while(stack and stack[-1][0] < n):
                num, index = stack.pop()
                ret[index] = (i - index)
            stack.append((n, i))
        return ret