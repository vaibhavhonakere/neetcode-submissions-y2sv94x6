class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = [0]
        def dfs(i, currSum):
            if(i == len(nums) and target == currSum):
                return 1
            if(i >= len(nums)):
                return 0
            return dfs(i + 1, currSum + nums[i]) + dfs(i + 1, currSum - nums[i])

        return dfs(0, 0)
        return count[0]