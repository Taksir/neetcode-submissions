class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1], [1]

        for i in range(len(nums) - 1):
            left.append(left[-1] * nums[i])

        for i in range(len(nums) - 1, 0, -1):
            right.append(right[-1] * nums[i])

        right = right[::-1]

        ans = []
        for i in range(len(left)):
            ans.append(left[i] * right[i])

        return ans