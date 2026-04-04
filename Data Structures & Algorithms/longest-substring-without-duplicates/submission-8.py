class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        left = 0
        retLength = 0
        for right in range(len(s)):
            while(s[right] in substring):
                substring.remove(s[left])
                left += 1
            
            substring.add(s[right])
            retLength = max(retLength, right - left + 1)
        return retLength