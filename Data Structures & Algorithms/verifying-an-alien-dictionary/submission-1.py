class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {}

        for i, n in enumerate(order):
            mapping[n] = i
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for j in range(len(word1)):
                if(j == len(word2)):
                    return False
                
                if(word1[j] != word2[j]):
                    if(mapping[word1[j]] > mapping[word2[j]]):
                        return False
                    break
        
        return True
