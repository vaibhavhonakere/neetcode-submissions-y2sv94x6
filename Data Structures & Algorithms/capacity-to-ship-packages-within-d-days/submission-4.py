class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total_weight = sum(weights)

        def calculate_sum(check_weight):
            total = 0
            d = 1 # the days 
            for w in weights:
                if(w > check_weight):
                    return False
                if(w + total <= check_weight):
                    total += w
                else:
                    if(d + 1 <= days):
                        d += 1
                        total = w 
                    else:
                        return False
            return True
            
        left = max(weights)
        right = total_weight
        least_weight_capacity = total_weight
        while(left <= right):
            mid = (left + right) // 2
            if(calculate_sum(mid)):
                least_weight_capacity = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return least_weight_capacity
