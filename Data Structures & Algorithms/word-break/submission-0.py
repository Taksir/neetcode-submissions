class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [-1] * (len(s) + 1)

        def dfs(i):
            if memo[i] != -1:
                return bool(memo[i])
            if i == len(s):
                memo[i] = 1
                return True

            for word in wordDict:
                if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                    if dfs(i + len(word)):
                        memo[i] = 1
                        return True
            memo[i] = 0
            return False

        return dfs(0)
