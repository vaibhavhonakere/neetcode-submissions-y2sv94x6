class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = {n: 0 for n in nums}
        for num in nums:
            count[num] += 1

        def dfs(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for n in count:
                if(count[n] > 0):
                    count[n] -= 1
                    perm.append(n)
                    dfs(perm)
                    perm.pop()
                    count[n] += 1

        dfs([])
        return res