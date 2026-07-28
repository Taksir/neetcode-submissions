class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join("%d:" % len(s) + s for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        while i < len(s):
            j = s.find(':', i)
            i = j + int(s[i:j]) + 1
            strs.append(s[j+1:i])

        return strs