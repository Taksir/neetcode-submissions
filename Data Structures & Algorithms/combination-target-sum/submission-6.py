class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        nums.sort() # allows the early break in line 14,15
        def dfs(i, total):
            if total == target:
                ans.append(subset.copy())
                return 
            if i == len(nums) or nums[i] + total > target:
                return

            subset.append(nums[i])
            dfs(i, total + nums[i])
            subset.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return ans