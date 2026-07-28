class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxL = 0

        l, r = 0, 0
        while r < len(s):
            if s[r] in charSet:
                while s[l] != s[r]:
                    charSet.remove(s[l])
                    l += 1
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            maxL = max(maxL, len(charSet))
            r += 1

        return maxL
            