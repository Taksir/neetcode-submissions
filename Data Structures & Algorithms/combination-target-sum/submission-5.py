class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        nums.sort()
        def dfs(i, total, subset):
            nonlocal ans
            if total == target: # what if cursum > target? handle during branching
                ans.append(subset.copy())
                return 
            if total > target:
                return
            for j in range(i, len(nums)):
                if nums[j] + total > target:
                    break
                subset.append(nums[j])
                dfs(j, total + nums[j], subset)
                subset.pop()

        dfs(0, 0, [])
        return ans