class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]

# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         if len(s1) + len(s2) != len(s3):
#             return False
#         dp = {}

#         def dfs(i1, i2):
#             if (i1, i2) in dp:
#                 return dp[(i1, i2)]
#             if i1 == len(s1) and i2 == len(s2): # make sure we only enter when valid
#                 return True
#             if i1 < len(s1) and s1[i1] == s3[i1 + i2] and dfs(i1 + 1, i2):
#                 return True
#             if i2 < len(s2) and s2[i2] == s3[i1 + i2] and dfs(i1, i2 + 1):
#                 return True
#             dp[(i1, i2)] = False
#             return False

        return dfs(0, 0)