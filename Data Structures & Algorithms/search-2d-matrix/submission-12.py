class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while(left <= right):
            mid = (left + right) // 2
            if(matrix[mid][0] > target):
                right = mid - 1
            elif(matrix[mid][-1] < target):
                left = mid + 1
            else:
                break
        
        if(not(left <= right)):
            return False
        
        left = 0
        right = len(matrix[0]) - 1
        while(left <= right):
            m = (left + right) // 2
            if(matrix[mid][m] == target):
                return True
            elif(matrix[mid][m] < target):
                left = m + 1
            else:
                right = m - 1
        return False
        