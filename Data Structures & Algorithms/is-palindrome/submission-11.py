class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1
        nums = s
        while(left <= right):
            while(left <= right and not(nums[left].isalnum())):
                left += 1
            while(left <= right and not(nums[right].isalnum())):
                right -= 1
            
            if(left > right):
                break
            
            # print(left, right)
            if(nums[left].lower() != nums[right].lower()):
                return False
            
            left += 1
            right -= 1

        
        return True