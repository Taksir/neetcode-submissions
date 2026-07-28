class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        starting_idx = 0
        maxLen = float('-inf')

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    starting_idx = l
                l -= 1
                r += 1

        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    starting_idx = l
                l -= 1
                r += 1

        return s[starting_idx : starting_idx + maxLen]