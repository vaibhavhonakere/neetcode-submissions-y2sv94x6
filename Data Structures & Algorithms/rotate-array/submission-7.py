class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = (k % N)

        # for i in range(k):
        #     tmp = nums[i]
        #     nums[i] = nums[(i + k)]
        #     nums[(i + k)] = tmp
        start = nums[:N - k]
        ending = nums[N - k:]

        # print(start, ending, N - k, N)
        for i in range(len(ending)):
            nums[i] = ending[i]
        
        # print(ending, start, (N - k), N)
        beg = 0
        for j in range(len(start)):
            nums[(beg + k)] = start[j]
            beg += 1
        