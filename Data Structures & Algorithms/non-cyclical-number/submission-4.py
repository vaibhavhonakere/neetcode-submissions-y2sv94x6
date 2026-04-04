class Solution:
    def isHappy(self, n: int) -> bool:
        
        def calcNum(n):
            ret = 0
            while(n > 0):
                ret += (n % 10)**2
                n = n // 10
            return ret
        

        slow = n
        fast = calcNum(n)

        while(slow != fast):
            slow = calcNum(slow)
            fast = calcNum(calcNum(fast))
        return fast == 1
