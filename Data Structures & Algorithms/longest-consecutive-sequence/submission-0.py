class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxlen = 0
        for n in nums:
            if n-1 in numset:
                continue
            curlen = 1
            newn = n + 1
            while newn in numset:
                curlen += 1
                newn += 1
            maxlen = max(maxlen, curlen)

        return maxlen
            