class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {} # (num : index)

        for i, n in enumerate(nums):
            if(n in mapping):
                if(abs(i - mapping[n]) <= k):
                    return True
            mapping[n] = i
        return False
        
