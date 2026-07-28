class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # memo[i][last] stores result for dfs(i, last)
        memo = [[-1] * (n + 1) for _ in range(n + 1)]

        def dfs(i: int, last: int) -> int:
            if i == n:
                return 0
            if memo[i][last] != -1:
                return memo[i][last]

            # Skip current element
            skip = dfs(i + 1, last)

            # Try to include current element if it's larger than the last picked
            include = 0
            if last == -1 or nums[i] > nums[last]:
                include = 1 + dfs(i + 1, i)

            memo[i][last] = max(skip, include)
            return memo[i][last]

        return dfs(0, -1)
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)
#         # memo[i][last+1] stores result for dfs(i, last)
#         memo = [[-1] * (n + 1) for _ in range(n)]

#         def dfs(i: int, last: int) -> int:
#             if i == n:
#                 return 0
#             if memo[i][last + 1] != -1:
#                 return memo[i][last + 1]

#             # Skip current element
#             skip = dfs(i + 1, last)

#             # Try to include current element if it's larger than the last picked
#             include = 0
#             if last == -1 or nums[i] > nums[last]:
#                 include = 1 + dfs(i + 1, i)

#             memo[i][last + 1] = max(skip, include)
#             return memo[i][last + 1]

#         return dfs(0, -1)