class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_index = {c: i for i, c in enumerate(s)}

        ret = []
        start = 0
        subs_target = float("-inf")
        for i, char in enumerate(s):
            target_index = char_index.get(char)
            subs_target = max(subs_target, target_index)
            if(subs_target == i):
                ret.append(target_index - start + 1)
                start = target_index + 1
                subs_target = float("-inf")
        
        return ret
