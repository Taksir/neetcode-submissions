class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftMul, rightMul = [1], [1]

        for i in range(len(nums) - 1):
            leftMul.append(leftMul[-1] * nums[i])

        for i in range(len(nums) - 1, 0, -1):
            rightMul.append(rightMul[-1] * nums[i])

        rightMul = rightMul[::-1]

        ans = []
        for i in range(len(nums)):
            ans.append(leftMul[i] * rightMul[i])

        return ans