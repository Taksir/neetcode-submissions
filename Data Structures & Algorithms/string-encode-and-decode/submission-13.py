class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(["%d:" % len(s) + s for s in strs])
    def decode(self, s: str) -> List[str]:
        r = 0
        res = []
        while r < len(s):
            index = s.find(':', r)
            length = int(s[r:index])
            string = s[index + 1: index + 1 + length]
            res.append(string)
            r = index + 1 + length

        return res