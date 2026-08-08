class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset = []
        ans = []
        nums.sort()

        def dfs(idx, total):
            if total == target:
                ans.append(subset[:])
                return
            if total > target or idx == len(nums):
                return
            
            subset.append(nums[idx])
            dfs(idx, total + nums[idx])
            subset.pop()
            dfs(idx + 1, total)
        
        dfs(0, 0)
        return ans