class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen, numSet = 0, set(nums)

        for n in numSet:
            if n - 1 not in numSet:
                curLen = 1
                while n + 1 in numSet:
                    n += 1
                    curLen += 1

                maxLen = max(maxLen, curLen)

        return maxLen

# TLE if loops is on nums instead of numSet!!!
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         maxLen, numSet = 0, set(nums)

#         for n in nums:
#             if n - 1 not in numSet:
#                 curLen = 1
#                 while n + 1 in numSet:
#                     n += 1
#                     curLen += 1

#                 maxLen = max(maxLen, curLen)

#         return maxLen