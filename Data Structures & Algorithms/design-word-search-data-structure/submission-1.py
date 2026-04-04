class Trie:
    def __init__(self):
        self.neighbors = {}
        self.isLast = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if(w not in curr.neighbors):
                curr.neighbors[w] = Trie()
            curr = curr.neighbors[w]
        curr.isLast = True
    
    def search(self, word: str) -> bool:
        def dfs(index, root):
            curr = root
            for w in range(index, len(word)):
                char = word[w]
                if(char == "."):
                    for child in curr.neighbors.values():
                        if(dfs(w + 1, child)):
                            return True
                    return False
                else:
                    if(char not in curr.neighbors):
                        return False
                    curr = curr.neighbors[char]
            return curr.isLast
        return dfs(0, self.root)
