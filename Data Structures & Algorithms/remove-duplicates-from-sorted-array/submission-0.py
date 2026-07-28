class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        while r < len(nums):
            if r > 0 and nums[r] != nums[r-1]:
                l += 1
                nums[l] = nums[r]
            r += 1
        return l + 1