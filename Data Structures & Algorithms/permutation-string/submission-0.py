from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = Counter(s1)
        l, r = 0, len(s1) - 1

        while r < len(s2):
            count2 = Counter(s2[l:r+1])
            if count2 == count1:
                return True
            l += 1
            r += 1

        return False
