class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def options(code):
            res = []

            for i in range(4):
                digit = str((int(code[i]) + 1) % 10)
                res.append(code[:i] + digit + code[i+1:])
                digit = str(((int(code[i]) - 1) + 10) % 10)
                res.append(code[:i] + digit + code[i+1:])
            return res
        

        queue = deque([])
        queue.append(["0000", 0])
        visit = set(deadends)

        while(queue):
            for i in range(len(queue)):
                seq, turns = queue.popleft()
                if(seq == target):
                    return turns
                vals = options(seq)
                for opt in vals:
                    if(opt in visit):
                        continue
                    queue.append([opt, turns + 1])
                    visit.add(opt)
        return -1









