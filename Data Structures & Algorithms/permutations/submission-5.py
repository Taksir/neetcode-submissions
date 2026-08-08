class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        subset = []
        ans = []
        flags = [False] * len(nums)

        def dfs(flags):
            if len(subset) == len(nums):
                ans.append(subset[:])
                return

            for idx in range(len(nums)):
                if not flags[idx]:
                    subset.append(nums[idx])
                    flags[idx] = True
                    dfs(flags)

                    subset.pop()
                    flags[idx] = False

        dfs(flags)
        return ans