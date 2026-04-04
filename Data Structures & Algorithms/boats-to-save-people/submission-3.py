class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        # print(people)
        count = 0
        while(left <= right):
            person_1 = people[left]
            person_2 = people[right]

            if(person_1 + person_2 <= limit):
                count += 1
                left += 1
                right -= 1
            elif(person_2 <= limit):
                right -= 1
                count += 1
    
        return count
            