class Solution:
    def countSubstrings(self, s: str) -> int:
        num_palindromic_substrings = 0

        for ptr in range(len(s)):
            i = j = ptr
            while(i >= 0 and j < len(s) and s[i] == s[j]):
                num_palindromic_substrings += 1
                i -= 1
                j += 1
            
            i = ptr
            j = ptr + 1
            while(i >= 0 and j < len(s) and s[i] == s[j]):
                num_palindromic_substrings += 1
                i -= 1
                j += 1

        return num_palindromic_substrings
