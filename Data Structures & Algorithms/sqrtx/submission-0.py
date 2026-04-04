class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = 0
        while(l <= r):
            m = (l + r) // 2
            candidate = m * m
            if(candidate > x):
                r = m - 1
            elif(candidate < x):
                res = m
                l = m + 1
            else:
                return m
        return res