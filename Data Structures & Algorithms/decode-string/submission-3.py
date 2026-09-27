class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if(char == "]"):
                # we are trying to find the characters now
                sequence_chars = ""
                while(stack and stack[-1] != "["):
                    c = stack.pop()
                    sequence_chars += c
                sequence_chars = sequence_chars[::-1]
                stack.pop()
                digit = ""
                while(stack and stack[-1].isdigit()):
                    digit += stack.pop()
                
                # print("the digit ", digit, " the sequence_chars ", sequence_chars)
                digit = int(digit[::-1])
                characters = digit * sequence_chars
                for c in characters:
                    stack.append(c)
                # print(stack)
            else:
                stack.append(char)
        
        return "".join(stack)


