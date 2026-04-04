class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if(sum(nums) % 2 != 0):
            return False
        
        target = sum(nums) // 2
        hashMap = {}

        def dfs(i, sumVal):
            if(sumVal == target):
                return True
            if(i == len(nums) or sumVal > target):
                return False
            
            hashMap[i] = dfs(i + 1, sumVal + nums[i]) or dfs(i + 1, sumVal)
            return hashMap[i]

        return dfs(0, 0)


            