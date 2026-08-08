class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # numSet = set()
        # for n in nums:
        #     if n in numSet:
        #         return n
        #     numSet.add(n)

        for i, num in enumerate(nums):
            index = abs(num) - 1
            if nums[index] < 0:
                return abs(num)
            nums[index] *= -1
