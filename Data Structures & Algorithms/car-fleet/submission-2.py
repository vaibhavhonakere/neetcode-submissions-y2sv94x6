class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        # print(pair)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            time = (target - p) / s
            if(stack and stack[-1] >= time):
                continue
            else:
                stack.append((target - p) / s)
            # if len(stack) >= 2 and stack[-1] <= stack[-2]:
            #     stack.pop()
        return len(stack)