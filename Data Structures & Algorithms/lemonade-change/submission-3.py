class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar = 0
        ten_dollar = 0
        twenty_dollar = 0

        for b in bills:
            if(b == 5):
               five_dollar += 1
            elif(b == 10):
                if(five_dollar <= 0):
                    return False
                else:
                    five_dollar -= 1
                    ten_dollar += 1
            elif(b == 20):
                if(five_dollar > 0 and ten_dollar > 0):
                    five_dollar -= 1
                    ten_dollar -= 1
                elif(five_dollar > 2):
                    five_dollar -= 3
                else:
                    return False
        
        return True
