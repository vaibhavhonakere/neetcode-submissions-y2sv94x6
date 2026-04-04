class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashMap = {}
        def dfs(ptr, currStr):
            if(ptr == len(s)):
                return True
            if(ptr in hashMap):
                return hashMap[ptr]
            # if(ptr > len(s)):
            #     return False
            print(currStr)
            hashMap[ptr] = False
            for word in wordDict:
                print(word, word == s[ptr: ptr + len(word)])
                if(ptr + len(word) <= len(s) and word == s[ptr: ptr + len(word)]):
                    currStr.append(s[ptr: ptr + len(word)])
                    if(dfs(ptr + len(word), currStr)):
                        hashMap[ptr] = True
                        break
                    currStr.pop()
            return hashMap[ptr]
        return dfs(0, [])
        #return check[0]