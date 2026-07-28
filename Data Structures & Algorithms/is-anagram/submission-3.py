# from collections import Counter
# return Counter(s) == Counter(t)

class Solution: 
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars_s, chars_t = [0] * 26, [0] * 26
        for i in range(len(s)):
            chars_s[ord(s[i]) - ord('a')] += 1
            chars_t[ord(t[i]) - ord('a')] += 1

        for i in range(26):
            if chars_s[i] != chars_t[i]:
                return False
        return True