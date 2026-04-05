class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        min_val = float("inf")
        arr = nums
        while(left <= right):
            mid = (left + right) // 2

            if(arr[left] <= arr[mid]):
                min_val = min(arr[left], min_val)
            
            if(arr[mid] > arr[right]):
                left = mid + 1
            else:
                min_val = min(arr[mid], min_val)
                right = mid - 1
        
        return min_val