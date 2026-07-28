class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for n in numSet:
            if n - 1 not in numSet:
                curLen = 1
                while n + 1 in numSet:
                    curLen += 1
                    n += 1
                maxLen = max(maxLen, curLen)

        return maxLen