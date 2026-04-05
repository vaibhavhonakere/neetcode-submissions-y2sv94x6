class Solution:
    def simplifyPath(self, path: str) -> str:
        print(path.split("/"))

        split_paths = path.split("/")
        stack = []
        for p in split_paths:
            if(p == "" or p == "."):
                continue
            elif(p == ".."):
                if(stack): stack.pop()
            else:
                stack.append(p)
        
        return "/" + "/".join(stack)

            
            
