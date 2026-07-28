from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ansDict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
                
            ansDict[tuple(count)] = ansDict.get(tuple(count), []) + [s]
        
        return list(ansDict.values())