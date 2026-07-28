from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for ch in string:
                count[ord(ch) - ord('a')] += 1
            myDict[tuple(count)].append(string)

        return list(myDict.values())