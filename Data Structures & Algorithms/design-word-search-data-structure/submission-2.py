class Trie:
    def __init__(self):
        self.children = {}
        self.isLast = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if(w not in curr.children):
                curr.children[w] = Trie()
            curr = curr.children[w]
        curr.isLast = True

    def search(self, word: str) -> bool:
        def dfs(i, newCurr):
            curr = newCurr
            for j in range(i, len(word)):
                if(word[j] == "."):
                    for posStart in curr.children:
                        if(dfs(j + 1, curr.children[posStart])):
                            return True
                    return False
                else:
                    if(word[j] not in curr.children):
                        return False
                    curr = curr.children[word[j]]
            return curr.isLast
        
        return dfs(0, self.root)
