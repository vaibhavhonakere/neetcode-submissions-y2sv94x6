class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,2,3,4,5,6,7,8,9]
        # [9,8,7,6,5,4,3,2,1]
        N = len(nums)
        k = k % N

        # first_half = nums[:N - k]
        # second_half = nums[N - k:]

        # for i in range(N - k):
        #     nums[(i + k) % N] = first_half[i]
        
        # for j in range(k):
        #     nums[j] = second_half[j]
        nums.reverse()
        tmp = k - 1
        for i in range(k - 1):
            if(i > tmp):
                break
            nums[i], nums[tmp] = nums[tmp], nums[i]
            tmp -= 1
        
        last = len(nums) - 1
        for j in range(k, len(nums) - 1):
            # print(j, last, nums)
            if(j > last):
                break
            nums[j], nums[last] = nums[last], nums[j]
            last -= 1
        # print(nums)

