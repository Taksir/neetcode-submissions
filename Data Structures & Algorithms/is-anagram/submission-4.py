class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sc, tc = [0] * 26, [0] * 26

        for i, ch in enumerate(s):
            sc[ord(s[i]) - ord('a')] += 1
            tc[ord(t[i]) - ord('a')] += 1

        for i in range(26):
            if sc[i] != tc[i]:
                return False
        
        return True