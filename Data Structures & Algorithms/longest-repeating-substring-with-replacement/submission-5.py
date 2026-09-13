class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # len(substring) - maxFreq > k
        left = 0
        char_freq = {}
        max_freq = float("-inf")
        longest_character = 0

        for right in range(len(s)):
            char_freq[s[right]] = char_freq.get(s[right], 0) + 1
            max_freq = max(max_freq, char_freq[s[right]])

            if(right - left + 1 - max_freq > k):
                char_freq[s[left]] -= 1
                left += 1
            
            longest_character = max(longest_character, right - left + 1)
        
        return longest_character
            

