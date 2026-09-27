class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # first find the correct row the number would fall under

        left = 0
        right = len(matrix) - 1
        mid = 0

        while(left <= right):
            mid = (left + right) // 2
            if(matrix[mid][0] > target):
                right = mid - 1
            elif(matrix[mid][-1] < target):
                left = mid + 1
            else:
                break
        
        left = 0
        right = len(matrix[mid]) - 1

        while(left <= right):
            m = (left + right) // 2
            if(matrix[mid][m] > target):
                right = m - 1
            elif(matrix[mid][m] < target):
                left = m + 1
            else:
                return True
        
        return False
        