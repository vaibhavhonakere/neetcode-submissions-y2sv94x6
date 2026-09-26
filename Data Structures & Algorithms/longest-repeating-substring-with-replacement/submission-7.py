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
            while((right - left + 1) - max_freq > k):
                char = s[left]
                char_freq[char] -= 1
                # if(char_freq[char] == 0):
                #     del char_freq[char]
                left += 1
            
            longest_character = max(longest_character, right - left + 1)
            
        
        return longest_character
            

