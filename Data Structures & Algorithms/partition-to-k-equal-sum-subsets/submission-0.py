class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        nums.sort(reverse=True)
        target = sum(nums) // k
        used = [False] * len(nums)
        ret = []

        def backtrack(i, subset, subsetSum):
            # if k == 0:
            #     return True
            if subsetSum == target:
                ret.append(subset)
                subset = []
                # return backtrack(0, k - 1, 0)
            if(i == len(nums)):
                return len(ret) == k

            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                used[j] = True
                subset.append(nums[i])
                if backtrack(j + 1, subset, subsetSum + nums[j]):
                    return True
                subset.pop()
                used[j] = False
            return False

        return backtrack(0, [], 0)