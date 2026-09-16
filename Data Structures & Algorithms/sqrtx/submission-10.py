class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        possible_ans = 0

        while(left <= right):
            mid = (left + ((right - left) // 2))

            squared_value = mid**2
            # print(squared_value)
            if(squared_value == x):
                return mid
            
            elif(squared_value < x):
                possible_ans = mid
                left = mid + 1
            else:
                right = mid - 1
            
        return possible_ans