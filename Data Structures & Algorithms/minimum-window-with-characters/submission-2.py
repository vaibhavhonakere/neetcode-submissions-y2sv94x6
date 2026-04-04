class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = 0
        patternMap = {}
        normalMap = {}
        l = 0
        minAmount = 10000
        for c in t:
            patternMap[c] = patternMap.get(c, 0) + 1
        
        minAmount = min(patternMap.values())
        
        need = len(patternMap.keys())
        # print(need)
        minLength = float("inf")
        ret = ""
        
        for r in range(len(s)):
            normalMap[s[r]] = normalMap.get(s[r], 0) + 1
            if(s[r] in patternMap and patternMap[s[r]] == normalMap[s[r]]):
                have += 1
            
            while(have == need):
                # print(patternMap)
                # print(normalMap)
                if(r - l + 1 < minLength):
                    minLength = min(minLength, r - l + 1)
                    ret = s[l: r + 1]
                normalMap[s[l]] -= 1
                if(s[l] in patternMap and patternMap[s[l]] > normalMap[s[l]]):
                    have -= 1
                if(normalMap[s[l]] == 0):
                    del normalMap[s[l]]
                l += 1
                # print("clear")
        
        return ret
            

        

