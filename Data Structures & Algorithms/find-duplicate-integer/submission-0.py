# neetcode youtube solution is hard. Check the Leetcode solution where num at index is mul by -1

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            idx = abs(n) - 1
            if nums[idx] < 0:
                return abs(n)
            
            nums[idx] *= -1
