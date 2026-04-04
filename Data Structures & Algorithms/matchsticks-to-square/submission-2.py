class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if(sum(matchsticks) % 4 != 0):
            return False
        matchsticks.sort(reverse = True)
        length = sum(matchsticks) // 4
        sides = [0] * 4

        def backtrack(j):
            if(j == len(matchsticks)):
                if(sides[0] == sides[1] == sides[2] == sides[3] == length):
                    return True
            if(j > len(matchsticks)):
                return False
            
            for i in range(4):
                if(matchsticks[j] + sides[i] <= length):
                    sides[i] += matchsticks[j]
                    if(backtrack(j + 1)):
                        return True
                    sides[i] -= matchsticks[j]
                if(sides[i] == 0):
                    break
            return False
        
        return backtrack(0)
            