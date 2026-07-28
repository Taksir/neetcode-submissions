class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def dfs(i, remaining):
            if remaining == 0:
                res.append(subset.copy())
                return
            if remaining < 0:
                return

            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j, remaining - nums[j])
                subset.pop()
        dfs(0, target)
        return res
