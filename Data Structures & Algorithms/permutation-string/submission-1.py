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
        
        s1_count = [0]*26
        s2_count = [0]*26

        # build out the mapping
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1
        
        matches = 0
        for i in range(26):
            if(s1_count[i] == s2_count[i]):
                matches += 1
        
        left = 0
        # print(matches)
        for right in range(len(s1), len(s2)):
            if(matches == 26):
                return True
            
            char = ord(s2[left]) - ord("a")
            s2_count[char] -= 1
            if(s2_count[char] + 1 == s1_count[char]):
                matches -= 1
            elif(s2_count[char] == s1_count[char]):
                matches += 1
            
            char = ord(s2[right]) - ord("a")
            s2_count[char] += 1
            if(s2_count[char] - 1 == s1_count[char]):
                matches -= 1
            elif(s2_count[char] == s1_count[char]):
                matches += 1
            
            left += 1

        # print(matches)
        return matches == 26
            
            





