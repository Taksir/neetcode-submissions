class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        subset = []
        ans = []

        def dfs(subset, flags):
            if len(subset) == len(nums):
                ans.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if not flags[i]:
                    flags[i] = True
                    subset.append(nums[i])
                    dfs(subset, flags)
                    subset.pop()
                    flags[i] = False

        dfs(subset, [False] * len(nums))
        return ans