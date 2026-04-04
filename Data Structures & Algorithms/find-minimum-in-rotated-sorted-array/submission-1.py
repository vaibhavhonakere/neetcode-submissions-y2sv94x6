class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        save = 0

        while(left < right):
            mid = (left + right) // 2

            if(nums[mid] > nums[right]):
                left = mid + 1
            else:
                save = mid
                right = mid
            # print(mid)
        
        return nums[right]