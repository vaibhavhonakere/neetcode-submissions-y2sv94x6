class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        right = len(matrix) - 1
        mid = None
        arr = matrix
        while(left <= right):
            mid = (left + right) // 2
            if(target < arr[mid][0]):
                right = mid - 1
            elif(target > arr[mid][-1]):
                left = mid + 1
            else:
                break
        
        left = 0
        right = len(matrix[0]) - 1
        m = mid

        while(left <= right):
            mid = (left + right) // 2
            if(target < arr[m][mid]):
                right = mid - 1
            elif(target > arr[m][mid]):
                left = mid + 1
            else:
                return True
        return False


