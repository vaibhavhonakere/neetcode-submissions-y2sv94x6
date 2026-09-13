class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # index_ones = []
        # for i, b in enumerate(boxes):
        #     if b == "1":
        #         index_ones.append(i)

        # num_of_ops = []
        # for i, b in enumerate(boxes):
        #     res = 0
        #     for ones_index in index_ones:
        #         res += abs(ones_index - i)
        #     num_of_ops.append(res)
        
        # return num_of_ops

        res = [0] * len(boxes)

        balls, moves = 0, 0
        for i in range(len(boxes)):
            res[i] += balls + moves
            moves = balls + moves
            balls += int(boxes[i])

        balls, moves = 0, 0
        for i in range(len(boxes) -1, -1, -1):
            res[i] += balls + moves
            moves = balls + moves
            balls += int(boxes[i])
        
        return res


        

