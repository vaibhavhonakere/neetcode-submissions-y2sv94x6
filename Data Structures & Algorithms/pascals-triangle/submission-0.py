class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if(numRows == 1):
            return [[1]]
        
        if(numRows == 2):
            return [[1], [1,1]]
        

        ret = [[1], [1,1]]
        i = 2
        while(i < numRows):
            level = [1]
            tmp = ret[i - 1]
            for j in range(1, len(tmp)):
                level.append(tmp[j - 1] + tmp[j])
            level.append(1)
        
            ret.append(level)
            i += 1
        return ret
