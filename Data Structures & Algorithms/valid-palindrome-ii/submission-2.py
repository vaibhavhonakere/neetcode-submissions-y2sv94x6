class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while(left < right):
            if(s[left] == s[right]):
                left += 1
                right -= 1
            else:
                tmp1 = s[left: right]
                tmp2 = s[left + 1: right + 1]
                return tmp1[::-1] == tmp1 or tmp2[::-1] == tmp2
        
        return True

