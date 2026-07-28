class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                subS = s[i:j]
                # print(subS)
                if len(subS) == len(set(subS)):
                    ans = max(ans, len(subS))
        return ans