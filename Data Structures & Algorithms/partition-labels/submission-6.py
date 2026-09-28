class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_index = {c: i for i, c in enumerate(s)}

        ret = []
        start = 0
        subs_target = float("-inf")
        for i, char in enumerate(s):
            subs_target = max(subs_target, char_index[char])
            if(subs_target == i):
                ret.append(i - start + 1)
                start = i + 1
                subs_target = float("-inf")
        
        return ret
