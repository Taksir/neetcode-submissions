class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(nums):
            if len(nums) == 1:
                return nums[0]
            first, second = nums[0], max(nums[0], nums[1])
            for i in range(2, len(nums)):
                nxt = max(second, first + nums[i])
                first, second = second, nxt
            return second
        
        l, r = helper(nums[1:]), helper(nums[:-1])
        return max(l, r)