class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1
        while(left <= right):
            if(s[left] != s[right]):
                subLeft = s[left:right]
                subRight = s[left + 1: right + 1]
                return subLeft[::-1] == subLeft or subRight[::-1] == subRight
            left += 1
            right -= 1
        return True