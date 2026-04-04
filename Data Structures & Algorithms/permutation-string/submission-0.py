class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Have a count or the permutation and we can store it as a list
        # and can just check that with the pairing when we get close

        # For example, for "abc", we can calculate the ord for a, and store in 
        # a 26 character list...so it can be something like this
        # [1, 1, 1, 0, 0, ... 0] == "abc"
        #  0, 1, 2, 3, 4, ... 25 

        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        left = 0
        for right in range(len(s1), len(s2)):
            if(matches == 26):
                return True
            
            ch = ord(s2[right]) - ord('a')
    
            s2Count[ch] += 1
            if(s2Count[ch] - 1 == s1Count[ch]):
                matches -= 1
            elif(s2Count[ch] == s1Count[ch]):
                matches += 1
            
            ch = ord(s2[left]) - ord('a')
            s2Count[ch] -= 1
            if(s2Count[ch] + 1 == s1Count[ch]):
                matches -= 1
            elif(s2Count[ch] == s1Count[ch]):
                matches += 1
            
            left += 1
        
        return matches == 26

            





