class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        substring = set()
        longest_sub = 0

        for right in range(len(s)):
            while(s[right] in substring):
                substring.remove(s[left])
                left += 1
            
            substring.add(s[right])
            longest_sub = max(longest_sub, right - left + 1)

        return longest_sub