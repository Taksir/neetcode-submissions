class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        first = nums[0]
        second = max(first, nums[1]) # what if len(nums) == 2
        for i in range(2, len(nums)):
            nxt = max(second, first + nums[i])
            first, second = second, nxt
        
        return second