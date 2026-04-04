import random
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []
        def dfs(node):
            if(node in visited):
                return visited[node]
            
            visited[node] = True
            for n in adj[node]:
                if(dfs(n)):
                    return True
            visited[node] = False
            res.append(node)
            return False
        
        for x, y in adj.items():
            if(dfs(x)):
                return ""
        
        return "".join(res[::-1])

        # def dfs(char):
        #     if char in visited:
        #         return visited[char]

        #     visited[char] = True

        #     for neighChar in adj[char]:
        #         if dfs(neighChar):
        #             return True

        #     visited[char] = False
        #     res.append(char)
        #     return False

        # my_list = list(adj.keys())
        # random.shuffle(my_list)
        # for char in my_list:
        #     print(char)
        #     if dfs(char):
        #         return ""

        # res.reverse()
        # return "".join(res)