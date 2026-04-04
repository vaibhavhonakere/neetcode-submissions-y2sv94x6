class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while(l <= r):
            m = (l + r) // 2
            if(matrix[m][0] <= target <= matrix[m][-1]):
                break
            elif(matrix[m][0] < target):
                l = m + 1
            else:
                r = m - 1

        l, r = 0, len(matrix[0]) - 1
        while(l <= r):
            m2 = (l + r) // 2
            if(matrix[m][m2] == target):
                return True
            elif(matrix[m][m2] < target):
                l = m2 + 1
            else:
                r = m2 - 1
        print(m)
        return False
