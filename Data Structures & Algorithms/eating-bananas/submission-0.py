class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def timeToEatBananas(num):
            hours = 0
            for p in piles:
                hours += math.ceil(p / num)
            return hours
        
        l = 1
        r = max(piles)
        res = 0
        while(l <= r):
            m = (l + r) // 2 # this is the rate bananas-per-hour
            checkHours = timeToEatBananas(m)
            # print(m, checkHours) 
            if(checkHours <= h):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res