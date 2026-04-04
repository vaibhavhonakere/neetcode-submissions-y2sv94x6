class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ret = ""
        for i in range(len(s)):
            left = i
            right = i

            while(left >= 0 and right < len(s) and s[left] == s[right]):
                if(len(ret) < right - left + 1):
                    ret = s[left: right + 1]
                left -= 1
                right += 1
            
            left = i 
            right = i + 1
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                if(len(ret) < right - left + 1):
                    ret = s[left: right + 1]
                left -= 1
                right += 1

        return ret