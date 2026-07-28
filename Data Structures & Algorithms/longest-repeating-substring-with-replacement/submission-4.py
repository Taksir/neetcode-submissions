class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count = dict()
        ans = 0
        maxf = 0

        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            maxf = max(maxf, count[s[i]])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1

        return ans

