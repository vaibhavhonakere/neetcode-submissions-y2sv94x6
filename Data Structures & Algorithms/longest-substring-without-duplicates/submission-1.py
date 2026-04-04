class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        maxVal = 0
        left = 0
        for right, let in enumerate(s):
            while(s[right] in charset):
                charset.remove(s[left])
                left += 1
            charset.add(s[right])
            maxVal = max(maxVal, right - left + 1)
        return maxVal