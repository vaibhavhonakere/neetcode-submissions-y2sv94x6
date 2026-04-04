class Solution:
    def isValid(self, s: str) -> bool:
        map = {"]" : "[", "}":"{", ")":"("}
        stack = []
        for character in s:
            if(character in map):
                if(stack and stack[-1] == map[character]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)
        return False if(stack) else True