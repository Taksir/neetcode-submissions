# solve this too https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1
        for n in nums:
            temp = curMax * n
            curMax = max(n, curMax * n, curMin * n)
            curMin = min(n, temp, curMin * n)
            res = max(res, curMax)
        return res

# bad approach that does not work. tried recursion in vain
# import sys
# sys.setrecursionlimit(10001)

# from math import prod
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         memo = [[""] * (len(nums) + 1) for i in range(len(nums) + 1)]

#         def dfs(l, r):
#             if l < 0 or r > len(nums) - 1 or l > r :
#                 return 1
#             if memo[l][r] != "":
#                 return memo[l][r]
#             if l == r:
#                 memo[l][r] = nums[l]
#                 return memo[l][r]
#             elif l + 1 == r:
#                 memo[l][r] = max(nums[l] * nums[r], nums[l], nums[r])
#                 return memo[l][r]
            
#             selfp = l * dfs(l + 1, r)
#             left = dfs(l + 1, r)
#             right = dfs(l, r - 1)
#             memo[l][r] = max(selfp, left, right) 
#             return memo[l][r]

#         ans = dfs(0, len(nums) - 1)
#         return memo[0][len(nums) - 1]
