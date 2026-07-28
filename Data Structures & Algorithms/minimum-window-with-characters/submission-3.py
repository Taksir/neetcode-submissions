from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not t or not s:
            return ""

        tCount = Counter(t)
        required = len(tCount)
        formed = 0
        count = {}
        res = (float('infinity'), None, None)
        l, r = 0, 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            if s[r] in tCount and count[s[r]] == tCount[s[r]]:
                formed += 1
            
            while l <= r and formed == required:
                if r - l + 1 < res[0]:
                    res = (r-l+1, l, r)
                count[s[l]] -= 1
                if s[l] in tCount and count[s[l]] + 1 == tCount[s[l]]:
                    formed -= 1
                l += 1
            
        return s[res[1]: res[2]+1] if res[0] != float('infinity') else ""
                 

        # while r < len(s):
            # character = s[r]
            # count[character] = count.get(character, 0) + 1
            # if (
            #     character in tCount
            #     and count[character] == tCount[character]
            # ):
            #     formed += 1
            # while l <= r and formed == required:
            #     character = s[l]

            #     if r - l + 1 < res[0]:
            #         res = (r - l + 1, l, r)
            #     count[character] -= 1
            #     if (
            #         character in tCount
            #         and count[character] < tCount[character]
            #     ):
            #         formed -= 1
            #     l += 1

            # r += 1