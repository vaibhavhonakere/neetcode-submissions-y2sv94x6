class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_str = str1 if len(str1) < len(str2) else str2
        max_str = str2 if len(str1) < len(str2) else str1
        valid_res = ""
        for i in range(min(len(str1), len(str2))):
            copy = min_str[:i + 1]
            small_multiple = len(min_str) // len(copy)
            big_multiple = len(max_str) // len(copy)

            if(small_multiple * copy == min_str and big_multiple * copy == max_str):
                valid_res = copy
        return valid_res      
        
        