class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        count = dict()
        window = dict()
        have = 0
        l = 0
        resLen = float('inf')
        res = [-1, -1]
        for i in range(len(t)):
            count[t[i]] = count.get(t[i], 0) + 1
        need = len(count)

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in count and window[s[r]] == count[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen: # cld pssbly be a soln
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1

                l += 1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""
