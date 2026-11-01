class Solution:
    def reverseBits(self, n: int) -> int:



        ret = 0
        # while(n > 0):
        #     digit = n & 1
        #     ret 
        #     n = n >> 1

        for i in range(32):
            digit = n & 1
            # print(digit)
            ret |= digit << (31 - i) 
            n = n >> 1
        return ret