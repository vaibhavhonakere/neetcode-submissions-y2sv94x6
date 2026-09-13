class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k % N

        first_half = nums[:N - k]
        second_half = nums[N - k:]

        for i in range(N - k):
            nums[(i + k) % N] = first_half[i]
        
        for j in range(k):
            nums[j] = second_half[j]

