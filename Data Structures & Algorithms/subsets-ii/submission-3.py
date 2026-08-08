class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def dfs(idx, subset):
            if idx == len(nums):
                ans.append(subset[:])
                return

            subset.append(nums[idx])
            dfs(idx + 1, subset)

            subset.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            dfs(idx + 1, subset)


        dfs(0, [])
        return ans