class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        def backtrack(i, subset):
            nonlocal res
            if(len(subset) == k):
                res.append(subset.copy())
                return
    
            # subset.append(nums[i])
            # backtrack(i + 1, subset, subset_sum + nums[i])
            # subset.pop()
            # while(i + 1 < len(nums) and nums[i] == nums[i+1]):
            #     i += 1
            # backtrack(i + 1, subset, subset_sum)

            for j in range(i, n + 1):
                backtrack(j + 1, subset + [j])
        
        backtrack(1, [])
        return res