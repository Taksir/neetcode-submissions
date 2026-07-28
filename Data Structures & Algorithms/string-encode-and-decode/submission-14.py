class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(s)) + ':' + s for s in strs]) 
    def decode(self, s: str) -> List[str]:
        r = 0
        ans = []
        while r < len(s):
            idx = s.find(":", r)
            length = int(s[r: idx])
            slice = s[idx + 1 : idx + length + 1]
            ans.append(slice)
            r = idx + length + 1

        return ans