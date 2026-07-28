class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        nums.sort()

        def dfs(i, target, subset):
            if target == 0:
                ans.append(subset.copy())
                return
            # handle overflow
            for j in range(i, len(nums)):
                if target - nums[j] < 0:
                    break
                subset.append(nums[j])
                dfs(j, target - nums[j], subset)
                subset.pop()

        dfs(0, target, subset)
        return ans