class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        min_val = float("inf")
        arr = nums
        while(left <= right):
            mid = (left + right) // 2
            if(target == nums[mid]):
                return mid
            elif(nums[left] <= nums[mid]):
                if(nums[left] > target or nums[mid] < target):
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if(nums[right] < target or nums[mid] > target):
                    right = mid - 1
                else:
                    left = mid + 1

        return -1