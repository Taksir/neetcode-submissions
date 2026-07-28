class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        maxL = 0
        count = dict()
        maxFreq = 0

        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(maxFreq, count[s[r]])

            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            maxL = max(maxL, r - l + 1)
            r += 1

        return maxL