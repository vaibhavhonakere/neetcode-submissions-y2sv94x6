class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_str = str1 if len(str1) < len(str2) else str2
        max_str = str2 if len(str1) < len(str2) else str1
        valid_res = ""
        for i in range(min(len(str1), len(str2))):
            copy = min_str[:i+1]
            multiple = len(min_str) // len(copy)
            multiple_2 = len(max_str) // len(copy)
            if copy * multiple == min_str and copy * multiple_2 == max_str:
                valid_res = copy

        return valid_res      
        
        