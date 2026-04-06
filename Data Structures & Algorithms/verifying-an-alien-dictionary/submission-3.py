class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ord_index = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            first = words[i]
            second = words[i+1]

            for j in range(len(first)):
                if(j == len(second)):
                    return False
                
                if(first[j] != second[j]):
                    if(ord_index[first[j]] > ord_index[second[j]]):
                        return False
                    break
            
        return True
