class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]

        for i in range(len(nums) - 1):
            ans.append(ans[-1] * nums[i])
        
        val = nums[-1]
        for i in range(len(ans) - 2, -1, -1):
            ans[i] = val * ans[i]
            val = val * nums[i]

        # val = 1
        # for i in range(len(ans) - 1, -1, -1):
        #     ans[i] = val * ans[i]
        #     val = val * nums[i]

        return ans

        # 1 2 4 6 nums 
        # 1 2 8 24 ans
        # 