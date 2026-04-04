class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")]*(len(nums))
        dp[-1] = 0
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if(j + i < len(nums)):
                    dp[i] = min(dp[i], dp[j+i] + 1)
        return dp[0]