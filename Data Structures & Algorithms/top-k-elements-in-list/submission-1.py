class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nums_freq = [[] for _ in range(n + 1)]

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0) 

        for key,v in count.items():
            nums_freq[v].append(key)
        
        ret = []
        for i in range(len(nums_freq) - 1, 0, -1):
            for ele in nums_freq[i]:
                # print(ele, k)
                if(k > 0):
                    ret.append(ele)
                    k -= 1
                else:
                    break
        
        return ret
