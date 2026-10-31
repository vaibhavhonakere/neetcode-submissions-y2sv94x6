class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        matchsticks = nums
        total_length = sum(matchsticks)
        if total_length % k != 0:
            return False

        length = total_length // k
        sides = [0] * k
        matchsticks.sort(reverse=True)

        def dfs(i):
            if i == len(matchsticks):
                return True

            for side in range(k):
                if sides[side] + matchsticks[i] <= length:
                    sides[side] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[side] -= matchsticks[i]

                if sides[side] == 0:
                    break

            return False
        
        return dfs(0)