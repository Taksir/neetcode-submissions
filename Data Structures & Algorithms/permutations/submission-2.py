class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(perm, flags):
            if len(perm) == len(nums):
                ans.append(perm.copy())
                return
            for i in range(len(nums)):
                if not flags[i]:
                    flags[i] = True
                    perm.append(nums[i])
                    dfs(perm, flags)
                    perm.pop()
                    flags[i] = False

        dfs([], [False] * len(nums))
        return ans