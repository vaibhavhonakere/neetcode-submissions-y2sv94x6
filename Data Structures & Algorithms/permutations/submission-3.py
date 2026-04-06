class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def perms(nums):
            if(not(nums)):
                return [[]]

            ret = []
            first = nums.pop(0)
            perm = perms(nums)
            for p in perm:
                for i in range(len(p) + 1):
                    copy_p = p.copy()
                    copy_p.insert(i, first)
                    ret.append(copy_p)
            return ret
        
        return perms(nums)