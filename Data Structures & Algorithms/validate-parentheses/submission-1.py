class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for b in s:
            if b in mapping:
                if(stack and stack[-1] == mapping[b]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        
        return len(stack) == 0