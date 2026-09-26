class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # have a counter if the keys in the counter is greater than 2 
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

            if(len(count) < 3):
                continue
            
            tmp_count = defaultdict(int)
            for n, c in count.items():
                if(c > 1):
                    tmp_count[n] = c - 1
            count = tmp_count
        
        # print(count)
        ret = []
        for x,y in count.items():
            if(nums.count(x) > len(nums) // 3):
                ret.append(x)
        
        return ret
