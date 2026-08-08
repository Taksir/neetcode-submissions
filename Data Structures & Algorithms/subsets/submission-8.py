class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        ans = []

        def dfs(idx, subset):
            if idx == len(nums):
                ans.append(subset[:])
                return
            
            subset.append(nums[idx])
            dfs(idx + 1, subset)
            subset.pop()
            dfs(idx + 1, subset)

        dfs(0, subset)
        return ans