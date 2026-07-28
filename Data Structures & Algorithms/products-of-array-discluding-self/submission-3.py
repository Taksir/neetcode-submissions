class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] # ans array

        for num in nums[:-1]:
            left.append(left[-1] * num)
        right = 1
        # print(left)
        for i in reversed(range(len(nums))):
            left[i] = left[i] * right
            right *= nums[i]
            # print(left, right)
        
        return left
# 1 2 4 6 nums 
# 1 1 2 8 left
# 48 24 6 1 right
# 48 24 12 8 ans