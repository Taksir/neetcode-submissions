class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        maxF = 0
        l = r = 0
        ans = 0
        while r < len(s):
            counts[ord(s[r]) - ord('A')] += 1 
            maxF = max(maxF, counts[ord(s[r]) - ord('A')])
            while (r - l + 1) - maxF > k:
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1

            ans = max(ans, r - l + 1)
            r += 1
        return ans
