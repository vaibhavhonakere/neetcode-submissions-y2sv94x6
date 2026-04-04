class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = [0]
        def dfs(i, currSum, subset):
            if(i >= len(nums) and target == currSum):
                count[0] += 1
                return
            if(i >= len(nums)):
                return
            dfs(i + 1, currSum + nums[i], subset + [nums[i]])
            dfs(i + 1, currSum - nums[i], subset + [-nums[i]])

        dfs(0, 0, [])
        return count[0]