class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [[-1] * (len(nums) + 1) for i in range(len(nums) + 1)]
        def dfs(i, last):
            if i == len(nums):
                return 0
            if memo[i][last] != -1:
                return memo[i][last]
            
            skipped = dfs(i + 1, last)

            included = 0
            if last == -1 or nums[i] > nums[last]:
                included = 1 + dfs(i + 1, i)
            memo[i][last] = max(skipped, included)
            return memo[i][last]

        return dfs(0, -1)