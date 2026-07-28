class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = r = 0
        ans = 0
        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            ans = max(ans, r - l + 1)
            r += 1

        return ans