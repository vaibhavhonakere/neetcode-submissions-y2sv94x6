class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_longest_substring = 0
        left = 0
        subset_set = set()
        
        for right in range(len(s)):
            while(s[right] in subset_set):
                subset_set.remove(s[left])
                left += 1

            max_longest_substring = max(max_longest_substring, right - left + 1)
            subset_set.add(s[right])
        
        return max_longest_substring
