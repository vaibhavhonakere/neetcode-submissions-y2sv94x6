class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def numOnes(n):
            count = 0

            while(n > 0):
                count += (n & 1)
                n >>= 1

            return count
        
        ret = []
        for i in range(n + 1):
            ret.append(numOnes(i))
        
        return ret