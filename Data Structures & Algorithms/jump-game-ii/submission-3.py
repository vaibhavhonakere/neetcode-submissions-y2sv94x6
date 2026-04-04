class Solution:
    def jump(self, nums: List[int]) -> int:
        #  0 1 2 3 4 5
        # [2,4,1,1,1,1]
        # [2,1,3,2,1,1].     dp[i] = min(dp[i], 1 + dp[j])

        dp = [float("inf") for i in range(len(nums))]
        dp[len(nums) - 1] = 0

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if(i + nums[i] >= j):
                    dp[i] = min(dp[i], 1 + dp[j])
            

        return dp[0]