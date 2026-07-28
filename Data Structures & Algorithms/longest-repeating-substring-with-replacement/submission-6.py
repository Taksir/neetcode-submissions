class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxF = 0

        for r, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            maxF = max(maxF, count[ch])

            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res