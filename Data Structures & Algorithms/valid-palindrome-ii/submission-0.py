class Solution:
    def validPalindrome(self, s: str) -> bool:

        for i in range(len(s)):
            newStr = s[:i] + s[i + 1:]
            if(newStr[::-1] == newStr):
                return True
        return False