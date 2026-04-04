class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if(char == "]"):
                word = ""
                while(stack and stack[-1] != "["):
                    word = str(stack.pop()) + word
                
                stack.pop()
                num = ""
                while(stack and stack[-1].isdigit()):
                    num = str(stack.pop()) + num
                
                num = int(num)
                stack.append(num * word)
            else:
                stack.append(char)
        
        return "".join(stack)