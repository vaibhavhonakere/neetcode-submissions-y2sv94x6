class Solution:
    def findMin(self, nums: List[int]) -> int:
        arr = nums
        l = 0
        r = len(nums) - 1
        minVal = float("inf")
        while(l <= r):
            m = (l + r) // 2
            if(arr[l] <= arr[m]):
                minVal = min(minVal, arr[l])
                l = m + 1
            else:
                minVal = min(minVal, arr[m])
                r = m - 1
        return minVal
