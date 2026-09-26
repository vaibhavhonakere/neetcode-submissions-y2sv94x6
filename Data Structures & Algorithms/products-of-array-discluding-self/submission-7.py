class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]

        # [1,1,2,8]
        # [48,24,6,1]

        tmp_1 = [1]
        tmp_2 = deque([1])
        for i in range(len(nums) - 1):
            tmp_1.append(tmp_1[-1] * nums[i])
        
        for j in range(len(nums)-1, 0, -1):
            tmp_2.appendleft(tmp_2[0] * nums[j])
        
        ret = []
        for l, r in zip(tmp_1, tmp_2):
            ret.append(l * r)
        
        return ret