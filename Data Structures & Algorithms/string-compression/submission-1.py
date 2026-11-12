class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = k = 0

        while(i < n):
            chars[k] = chars[i]
            beg = chars[i]
            k += 1
            j = i + 1
            while(j < n and beg == chars[j]):
                j += 1
            if(abs(j - i) > 1):
                num = abs(j - i)
                char_num = str(num)
                for c in char_num:
                    chars[k] = c
                    k += 1
            i = j
        
        return k
