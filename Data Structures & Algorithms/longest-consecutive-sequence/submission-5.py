class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen, numSet = 0, set(nums)

        for n in nums:
            if n - 1 in numSet:
                continue
            
            curLen = 0
            while n in numSet:
                n += 1
                curLen += 1

            maxLen = max(maxLen, curLen)

        return maxLen