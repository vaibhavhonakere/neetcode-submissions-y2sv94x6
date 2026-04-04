class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
        # [1, 1 ,2 ,8] Forward Pass
        # [48,48,24,6] Backward Pass
        # [24 24 ,12 8]

        res = [1] * (len(nums))

        res = [1]*(len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

        # forwardPass = [1]
        # backwardPass = [nums[-1]]
        # for n in nums:
        #     forwardPass.append(forwardPass[-1]*n)
        # forwardPass.pop()
        
        # for n in range(len(nums) - 2, -1, -1):
        #     backwardPass.append(backwardPass[-1]*nums[n])
        
        # backwardPass = backwardPass[::-1]
        # res = []
        # for i in range(len(forwardPass) - 1):
        #     res.append(forwardPass[i] * backwardPass[i + 1])
        # res.append(forwardPass[-1])
        # return res
