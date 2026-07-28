class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(["%d:" % len(s) + s for s in strs])
    def decode(self, s: str) -> List[str]:
        
        r = 0
        ans = []
        while r < len(s):
            idx = s.find(':', r)
            length = int(s[r:idx])
            string = s[idx + 1 : idx + length + 1]
            ans.append(string)
            r = idx + length + 1

        return ans