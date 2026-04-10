class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # These will be the actual indexes of the numbers that will be increasing
        monotonic_stack = deque([])
        ret = []
        left = 0
        for r in range(len(nums)):
            while(monotonic_stack and nums[monotonic_stack[-1]] <= nums[r]):
                monotonic_stack.pop()
            
            monotonic_stack.append(r)
            if(left > monotonic_stack[0]):
                monotonic_stack.popleft()
            
            if((r - left) + 1>= k):
                ret.append(nums[monotonic_stack[0]])
                left += 1
        
        return ret