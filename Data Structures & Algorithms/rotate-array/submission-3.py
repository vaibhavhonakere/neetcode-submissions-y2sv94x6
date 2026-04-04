class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Reverse the array 3 times 
        # first normal reversal
        nums.reverse()
        
        k = k % len(nums)
        j = k - 1
        for i in range(k // 2):
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1

        a = k
        j = len(nums) - 1

        for i in range((len(nums) - k) // 2):
            nums[a], nums[j] = nums[j], nums[a]
            j -= 1
            a += 1
        
        


        
        