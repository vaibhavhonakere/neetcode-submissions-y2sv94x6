class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def paranthesis(subset, closed_brackets, open_brackets):
            nonlocal ret
            if(closed_brackets == n):
                sub_copy = subset.copy()
                ret.append("".join(sub_copy))
                return ret
            
            if(open_brackets < n):
                subset.append("(")
                paranthesis(subset, closed_brackets, open_brackets + 1)
                subset.pop()
            
            if(open_brackets > closed_brackets):
                subset.append(")")
                paranthesis(subset, closed_brackets + 1, open_brackets)
                subset.pop()
            
            return
        
        paranthesis([], 0, 0)
        return ret