class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        ret = 0
        def dfs(i, sumV):
            nonlocal ret
            if(i == len(nums)):
                ret += sumV
                return 
            
            dfs(i + 1, sumV ^ nums[i])
            dfs(i + 1, sumV)
        
        dfs(0, 0)
        return ret