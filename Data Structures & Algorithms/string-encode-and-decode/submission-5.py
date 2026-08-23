class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for word in strs:
            ret += str(len(word)) + "#" + word
        return ret

    def decode(self, s: str) -> List[str]:
        # \print(s)
        i = 0
        ret = []
        while(i < len(s)):
            j = i
            while(s[j] != "#"):
                # print("hi", s[j])
                j += 1
            
            # print(s[i: i + j])
            num = int(s[i: j])
            i = j + 1
            word = ""
            for _ in range(num):
                # print(s[i])
                word += s[i]
                i += 1
            
            ret.append(word)
            # print(word)
            # print(i)
        
        return ret

            
