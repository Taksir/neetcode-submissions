class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # l2r, r2l, ans = [0] * len(nums), [0] * len(nums), [0] * len(nums)
        # l2r[0] = 1
        # for i in range(1, len(nums)):
        #     l2r[i] = l2r[i-1] * nums[i-1]

        # r2l[-1] = 1
        # for i in range(len(nums) - 2, -1, -1):
        #     r2l[i] = r2l[i+1] * nums[i+1]

        # for i in range(len(nums)):
        #     ans[i] = l2r[i] * r2l[i]

        # return ans

        mulLeft, mulRight = [], []

        left = right = 1
        for num in nums:
            mulLeft.append(left)
            left *= num
        
        i = 0
        for num in nums[::-1]:
            mulLeft[-i-1] *= right
            right *= num
            i += 1
        
        return mulLeft