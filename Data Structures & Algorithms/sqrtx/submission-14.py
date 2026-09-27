class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x + 1

        while left < right:
            mid = left + (right - left) // 2

            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid

        return left - 1
        
        # left = 0
        # right = x
        # possible_ans = 0

        # while(left < right):
        #     mid = (left + ((right - left) // 2))

        #     squared_value = mid**2

        #     if(squared_value <= x):
        #         #possible_ans = mid
        #         left = mid + 1
        #     else:
        #         right = mid
            
        # return left - 1 if(left - 1 > 0) else 0