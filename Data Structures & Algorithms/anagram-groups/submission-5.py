class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tuple2Strings = collections.defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for ch in s:
                counts[ord(ch) - ord('a')] += 1
            tuple2Strings[tuple(counts)].append(s)

        return list(tuple2Strings.values())