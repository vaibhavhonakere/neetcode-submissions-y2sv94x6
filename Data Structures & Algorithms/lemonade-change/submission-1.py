class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = {
            5: 0,
            10: 0,
        }
        

        for b in bills:
            if(b == 5):
                count[b] += 1
            elif(b == 10):
                if(count[5] > 0):
                    count[5] -= 1
                    count[b] += 1
                else:
                    return False
            elif(b == 20):
                if(count[10] > 0 and count[5] > 0):
                    count[5] -= 1
                    count[10] -= 1
                elif(count[5] > 2):
                    count[5] -= 3
                else:
                    return False
        
        return True




