class Trie:
    def __init__(self):
        self.lastWord = False
        self.neighbors = [None] * 26

class PrefixTree:

    def __init__(self):
        self.root = Trie()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if(curr.neighbors[i] == None):
                curr.neighbors[i] = Trie()
            curr = curr.neighbors[i]
        curr.lastWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if(curr.neighbors[i] == None):
                return False
            curr = curr.neighbors[i]
        return curr.lastWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if(curr.neighbors[i] == None):
                return False
            curr = curr.neighbors[i]
        return True
        
        