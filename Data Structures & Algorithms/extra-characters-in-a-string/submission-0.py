class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLast = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if(w not in curr.children):
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.isLast = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if(w not in curr.children):
                return False
            curr = curr.children[w]
        return curr.isLast

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            if(w not in curr.children):
                return False
            curr = curr.children[w]
        return True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        # tree = PrefixTree()
        
        # for dic in dictionary:
        #     tree.insert(dic)
        
        # curr = tree.root
        words = set(dictionary)
        dp = {len(s) : 0}

        def dfs(i):
            if(i in dp):
                return dp[i]
            
            res = 1 + dfs(i + 1)
            for j in range(i, len(s)):
                if(s[i:j + 1] in words):
                    res = min(res, dfs(j + 1))
            dp[i] = res
            return dp[i]
        
        return dfs(0)

             





        