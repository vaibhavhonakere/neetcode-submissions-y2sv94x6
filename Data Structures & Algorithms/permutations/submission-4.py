class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def perms(nums):
            if(not(nums)):
                return [[]]

            ret = []
            perm = perms(nums[1:])
            for p in perm:
                for i in range(len(p) + 1):
                    copy_p = p.copy()
                    copy_p.insert(i, nums[0])
                    ret.append(copy_p)
            return ret
        
        return perms(nums)