class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        mapping = {0: 1}
        count = 0

        for n in nums:
            cur_sum += n
            check = cur_sum - k

            count += mapping.get(check,0)

            mapping[cur_sum] = 1 + mapping.get(cur_sum,0)
        
        return count
