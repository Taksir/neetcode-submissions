class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l2r, r2l, ans = [0] * len(nums), [0] * len(nums), [0] * len(nums)
        l2r[0] = 1
        for i in range(1, len(nums)):
            l2r[i] = l2r[i-1] * nums[i-1]

        r2l[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            r2l[i] = r2l[i+1] * nums[i+1]

        for i in range(len(nums)):
            ans[i] = l2r[i] * r2l[i]

        return ans