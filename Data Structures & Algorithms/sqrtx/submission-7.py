class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        closest_val = float("-inf")
        while(left <= right):
            mid = left + ((right - left) // 2)
            square_val = mid * mid
            if(square_val > x):
                right = mid - 1
            elif(square_val < x):
                left = mid + 1
                # print(mid)
                closest_val = max(closest_val, mid)
            else:
                return mid

        return closest_val
