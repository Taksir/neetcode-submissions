class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    def isAnagram(self, s: str, t: str) -> bool:
        # return list(sorted(s)) == list(sorted(t))
        # return s.sort() == t.sort()

        if len(s) != len(t):
            return False

        sCounter = dict()
        tCounter = dict()

        for i in range(len(s)):
            sCounter[s[i]] = sCounter.get(s[i], 0) + 1
            tCounter[t[i]] = tCounter.get(t[i], 0) + 1
        
        for i in range(len(s)):

            if s[i] not in tCounter or sCounter[s[i]] != tCounter[s[i]]:
                return False
        
        return True
        