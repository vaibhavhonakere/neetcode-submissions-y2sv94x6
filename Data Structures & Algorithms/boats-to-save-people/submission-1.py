class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        count = 0
        left = 0
        right = len(people) - 1
        while(left <= right):
            # if(people[right] == limit):
            #     count += 1
            #     right -= 1
            if(right == left and people[right] <= limit):
                count += 1
                break
            elif(people[right] + people[left] <= limit):
                count += 1
                right -= 1
                left += 1
            elif(people[left] + people[right] > limit):
                count += 1
                right -= 1
        
        return count