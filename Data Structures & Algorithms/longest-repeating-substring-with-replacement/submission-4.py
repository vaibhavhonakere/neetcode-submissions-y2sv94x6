class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqChar = {}
        l = 0
        maxFreq = float("-inf")
        maxLength = float("-inf")
        for r in range(len(s)):
            freqChar[s[r]] = freqChar.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freqChar[s[r]])
            while((r - l + 1) - maxFreq > k):
                freqChar[s[l]] -= 1
                if(freqChar[s[l]] == 0):
                    del freqChar[s[l]]
                l += 1

            maxLength = max(maxLength, r - l + 1)
        
        return maxLength