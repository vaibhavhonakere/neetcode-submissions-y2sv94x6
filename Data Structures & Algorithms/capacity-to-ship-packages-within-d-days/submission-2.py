class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total_weight = sum(weights)

        def calculate_sum(check_weight):
            total = 0
            day = 1
            for w in weights:
                if(w > check_weight):
                    return False
                if(total + w <= check_weight):
                    total += w
                else:
                    if(day + 1 <= days):
                        day += 1
                    else:
                        return False
                    total = w

            return True

        left = max(weights)
        right = total_weight
        least_weight_capacity = total_weight
        while(left < right):
            mid = (left + right) // 2
            if(calculate_sum(mid)):
                least_weight_capacity = mid
                right = mid
            else:
                left = mid + 1
        
        return least_weight_capacity
