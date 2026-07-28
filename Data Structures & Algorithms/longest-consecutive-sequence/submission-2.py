class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxlen = 0
        for n in nums:
            if n-1 in numset:
                continue
            curlen = 0
            while n in numset:
                curlen += 1
                n += 1
            maxlen = max(maxlen, curlen)

        return maxlen
            