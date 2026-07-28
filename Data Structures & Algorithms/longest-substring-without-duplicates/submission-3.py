class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        charset = set()
        l = r = 0
        while r < len(s):
            if s[r] in charset: # moving l logic
                while s[l] != s[r]:
                    charset.remove(s[l])
                    l += 1
                l += 1

            charset.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1 # r always moving

        return longest