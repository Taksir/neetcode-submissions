class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sDict, tDict = dict(), dict()

        for i, ch in enumerate(s):
            sDict[s[i]] = sDict.get(s[i], 0) + 1
            tDict[t[i]] = tDict.get(t[i], 0) + 1
        
        return sDict == tDict
        