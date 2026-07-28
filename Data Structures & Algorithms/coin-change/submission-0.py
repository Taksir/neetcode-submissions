class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount + 1)
        coins.sort(reverse = True)
        def dfs(amt):
            if amt == amount:
                return 0
            if amt > amount:
                return float('inf')
            if memo[amt] != -1:
                return memo[amt]

            ans = float('inf')
            for c in coins:
                ans = min(ans, 1 + dfs(amt + c))

            memo[amt] = ans
            return ans
        ans = dfs(0)
        return ans if ans != float('inf') else -1
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         memo = [-1] * (amount + 1)
#         coins.sort(reverse = True)
#         def dfs(amt, cns):
#             if amt == amount:
#                 return cns
#             if amt > amount:
#                 return 10001
#             if memo[amt] != -1:
#                 return memo[amt]

#             counts = []
#             for c in coins:
#                 counts.append(dfs(amt + c, cns + 1))

#             memo[amt] = min(counts)
#             return memo[amt]
#         ans = dfs(0, 0)
#         return ans if ans != 10001 else -1