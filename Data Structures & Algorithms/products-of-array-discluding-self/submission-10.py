class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]

        for i in range(len(nums) - 1): # exclude last elem
            ans.append(ans[-1] * nums[i])
        
        # ans = 1 1 2 8

        val = 1
        
        for i in range(len(nums) - 1, -1 , -1):
            ans[i] = val * ans[i]
            val *= nums[i]
        
        return ans