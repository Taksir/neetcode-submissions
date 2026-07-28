class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and nums[i] == nums[i-1]: # skips 2nd,3rd etc copies
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1 # stop at last copy
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1 # stop at first copy
                    l += 1
                    r -= 1

                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    r -= 1
        return ans