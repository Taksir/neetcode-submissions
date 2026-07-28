class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded = ""
        for s in strs:
            l = len(s)
            newS = "".join([str(l), '#', s])
            encoded += newS
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        count = ""
        while i < len(s):
            while s[i] != '#':
                count += s[i]
                i+= 1
            
            decoded.append(s[i+1: i+1+int(count)])
            i+= int(count) + 1
            count = ""
            
        return decoded


