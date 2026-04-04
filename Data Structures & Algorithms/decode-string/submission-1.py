class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        check = False
        ret = ""
        r = 0

        while(r < len(s)):
            if(s[r].isnumeric()):
                start = r
                while(s[start].isnumeric()):
                    start += 1
                length = int(s[r: start])
                stack.append([length, ""])
                r = start - 1
            elif s[r] == "[":
                check = True
            elif s[r] == "]" and stack:
                num, char = stack.pop()
                if(stack):
                    stack[-1][1] += "".join([char for i in range(num)])
                else:
                    ret += "".join([char for i in range(num)])
            elif check and stack:
                stack[-1][1] += s[r]
            else:
                ret += s[r]
                check = False
            r += 1

        if(stack):
            num, char = stack.pop()
            ret += char
            return ret
        return ret





        # for n in s:
        #     # print(n)
        #     if n in "1234567890":
        #         stack.append([int(n), ""])
        #     elif n == "[":
        #         check = True
        #     elif n == "]" and stack:
        #         num, char = stack.pop()
        #         if(stack):
        #             stack[-1][1] += "".join([char for i in range(num)])
        #         else:
        #             ret += "".join([char for i in range(num)])
        #     elif check and stack:
        #         stack[-1][1] += n
        #     else:
        #         ret += n
        #         check = False
        #     # print(stack)
        # if(stack):
        #     num, char = stack.pop()
        #     ret += char
        #     return ret
        # return ret