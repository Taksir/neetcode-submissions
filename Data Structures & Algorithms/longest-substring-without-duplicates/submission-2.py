class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        curSet = set()
        maxSoFar = 0
        while r < len(s):
            if s[r] not in curSet:
                curSet.add(s[r])
                maxSoFar = max(maxSoFar, len(curSet))
                r += 1
            else:
                while s[l] != s[r]:
                    curSet.remove(s[l])
                    l += 1
                l += 1
                curSet.add(s[r])
                r += 1
            
        return maxSoFar