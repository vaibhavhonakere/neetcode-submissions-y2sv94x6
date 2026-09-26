class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        for i in range(len(nums)):
            if(i > 0 and nums[i - 1] == nums[i]):
                continue
            org = i
            left = i + 1
            right = len(nums) - 1
            while(left < right):
                cur_sum = nums[org] + nums[left] + nums[right]
                if(cur_sum > 0):
                    right -= 1
                elif(cur_sum < 0):
                    left += 1
                else:
                    ret.append([nums[org], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while(left < right and nums[left] == nums[left - 1]):
                        left += 1
        
        return ret