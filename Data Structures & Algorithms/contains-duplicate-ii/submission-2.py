class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_index = {}

        for i in range(len(nums)):
            if(nums[i] in nums_index and abs(i - nums_index[nums[i]]) <= k):
                return True

            nums_index[nums[i]] = i
        
        return False

