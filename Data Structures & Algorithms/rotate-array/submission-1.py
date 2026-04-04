class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        last = len(nums) - 1
        for i in range(len(nums) // 2):
            nums[i], nums[last] = nums[last], nums[i]
            last -= 1

        last = k - 1
        for i in range(k // 2):
            nums[i], nums[last] = nums[last], nums[i]
            last -= 1
        #     print(nums[i], nums[last])
        #     print(nums)
        
        # print(nums)
        
        last = len(nums) - 1
        i = k
        # print("what ", k, (len(nums)-1 - k + 1))
        for _ in range((len(nums)-1 - k + 1) // 2):
            if(i < len(nums) and last >= 0):
                # print("here")
                nums[i], nums[last] = nums[last], nums[i]
                last -= 1
                i += 1
                # print(nums)
        
        