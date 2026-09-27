class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for n in operations:
            if(n not in ["+", "D", "C"]):
                stack.append(n)
            elif(n == "+"):
                first = int(stack[-1])
                second = int(stack[-2])
                stack.append(str(first + second))
            elif(n == "D"):
                first = int(stack[-1])
                # second = int(stack.pop())
                stack.append(str(first * 2))
            elif(n == "C"):
                stack.pop()
        
        sum_val = 0
        for num in stack:
            sum_val += int(num)
        
        return sum_val