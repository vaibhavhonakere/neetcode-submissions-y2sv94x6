class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        nums.sort(reverse=True)
        target = sum(nums) // k
        used = [False] * len(nums)

        def dfs(i, subsetSum, k):
            if(k == 0):
                return True
            
            if(subsetSum == target):
                return dfs(0, 0, k - 1)
            
            for j in range(i, len(nums)):
                if(used[j] or subsetSum + nums[j] > target):
                    continue
                
                used[j] = True
                if(dfs(j + 1, subsetSum + nums[j], k)):
                    return True
                used[j] = False
            
            return False
        
        return dfs(0, 0, k)
