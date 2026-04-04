class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret = []
        for i in range(min(len(word1), len(word2))):
            ret.append(word1[i])
            ret.append(word2[i])

        if(len(word1) == len(word2)):
            return "".join(ret)
        elif(len(word1) < len(word2)):
            ret += [word2[i] for i in range(len(word1), len(word2))]
        else:
            ret += [word1[i] for i in range(len(word2), len(word1))]
        return "".join(ret)