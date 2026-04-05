class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        min_val = float("inf")
        arr = nums
        while(left <= right):
            if(nums[left] < nums[right]):
                min_val = min(min_val, nums[left])
                break  
              
            mid = (left + right) // 2
            # if(arr[left] <= arr[mid]):
            #     min_val = min(arr[left], min_val)
            min_val = min(arr[mid], min_val)
            if(arr[mid] > arr[right]):
                left = mid + 1
            else:
                right = mid - 1
        
        return min_val