class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_to_list = {}
        for s in strs:
            # build out the key
            anagram_key = [0]*26
            for char in s:
                anagram_key[ord(char) - ord("a")] += 1
            
            anagram_key = tuple(anagram_key)
            if(anagram_key in anagrams_to_list):
                anagrams_to_list[anagram_key].append(s)
            else:
                anagrams_to_list[anagram_key] = [s]
        
        return list(anagrams_to_list.values())

