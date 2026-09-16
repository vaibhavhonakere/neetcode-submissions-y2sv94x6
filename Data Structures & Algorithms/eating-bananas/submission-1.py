class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def is_possible(rate):
            temp = h
            for p in piles:
                hours = math.ceil(p / rate)
                temp -= hours
                if(temp < 0):
                    return False
            
            return True

        left = 1
        right = max(piles)
        slowest_possible_rate = -1

        while(left <= right):
            mid = (left + right) // 2

            valid = is_possible(mid)

            if(valid):
                slowest_possible_rate = mid
                right = mid - 1
            else:
                left = mid + 1
            
        
        return slowest_possible_rate