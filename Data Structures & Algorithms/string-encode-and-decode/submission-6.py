class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s)) + "#" + s
        return ret

    def decode(self, s: str) -> List[str]:
        i = 0
        ret = []
        while(i < len(s)):
            beg = i
            while(beg < len(s) and s[beg] != "#"):
                beg += 1
            # print(i, beg)
            # print(s[i:beg])
            num = int(s[i: beg])
            i = beg + 1
            word = ""
            for j in range(i, i + num):
                word += s[j]
            
            ret.append(word) 
            i += num
        
        return ret

            
