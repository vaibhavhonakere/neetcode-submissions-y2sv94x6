class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # perform merge sort

        def merge_sort(left, right, arr):
            if(len(arr[left:right + 1]) == 1):
                return arr[left:right + 1]
            
            mid = (left + right) // 2
            left_arr = merge_sort(left, mid, arr)
            right_arr = merge_sort(mid + 1, right, arr)

            l = 0
            r = 0
            ret = []
            while(l < len(left_arr) and r < len(right_arr)):
                if(left_arr[l] < right_arr[r]):
                    ret.append(left_arr[l])
                    l += 1
                else:
                    ret.append(right_arr[r])
                    r += 1
            
            if(l < len(left_arr)):
                ret += left_arr[l:]

            if(r < len(right_arr)):
                ret += right_arr[r:]
            
            return ret

        return merge_sort(0, len(nums) - 1, nums)
