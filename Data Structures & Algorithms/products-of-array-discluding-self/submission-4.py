class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i in range(1, len(nums)):
            left.append(left[-1]* nums[i-1])

        m = 1
        for i in reversed(range(len(nums))):
            left[i] *= m
            m *= nums[i]
        return left

# 1 2 4 6 nums 
# 1 1 2 8 left
# 48 24 6 1 right
# 48 24 12 8 ans