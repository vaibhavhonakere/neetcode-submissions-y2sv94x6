class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if(len(arr) <= 1):
            return len(arr)
        
        max_length = 1
        length = 1
        sign = 0
        if(arr[1] > arr[0]):
            sign = 1
            length += 1
        elif(arr[1] < arr[0]):
            sign = -1
            length += 1

        for i in range(1, len(arr)):
            if(arr[i] == arr[i - 1]):
                sign = 0
                continue
            if(sign == 0):
                sign = 1 if arr[i] > arr[i - 1] else -1
                length = 2
            elif(arr[i] > arr[i - 1] and sign == -1):
                length += 1
                sign = 1
            elif(arr[i] < arr[i - 1] and sign == 1):
                length += 1
                sign = -1
            else:
                length = 2

            max_length = max(length, max_length)
        
        return max_length

            


