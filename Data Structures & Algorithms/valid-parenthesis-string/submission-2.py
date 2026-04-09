class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMax = 0
        leftMin = 0

        for par in s:
            if(par == "("):
                leftMax += 1
                leftMin += 1

            if(par == ")"):
                leftMax -= 1
                leftMin -= 1

            if(par == "*"):
                leftMax += 1
                leftMin -= 1

            if(leftMax < 0):
                return False
            
            if(leftMin < 0):
                leftMin = 0
        
        return leftMin == 0


