class Solution:
    def romanToInt(self, s: str) -> int:
        mapping_symbol_to_value = {
            "I": 1,
            "V": 5,
            "X": 10, 
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        ret = 0
        for i, symbol in enumerate(s):
            if(i + 1 < len(s) and mapping_symbol_to_value[s[i]] < mapping_symbol_to_value[s[i + 1]]):
                ret -= mapping_symbol_to_value[symbol]
            else:
                ret += mapping_symbol_to_value[symbol]
        
        return ret
