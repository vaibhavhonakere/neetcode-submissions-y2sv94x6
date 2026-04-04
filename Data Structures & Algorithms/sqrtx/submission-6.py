class Solution:
    def mySqrt(self, x: int) -> int:
        if(x == 0):
            return 0
        left = 0
        right = x
        while(left <= right):
            mid = (right + left) // 2
            val = mid * mid
            if(val > x):
                right = mid - 1
            elif(val < x):
                left = mid + 1
                res = mid
            else:
                return mid

        return res