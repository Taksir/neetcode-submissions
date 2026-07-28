class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l, r = 0, 0
        last_idx = collections.defaultdict(int)
        for i in range(len(s)):
            last_idx[s[i]] = i 
        print(last_idx)
        charset = set()
        have = 0
        ans = []
        for r in range(len(s)):
            charset.add(s[r])
            if last_idx[s[r]] == r:
                have += 1

            if len(charset) == have:
                ans.append(r - l + 1)
                charset = set()
                have = 0
                l = r + 1
        return ans
                

