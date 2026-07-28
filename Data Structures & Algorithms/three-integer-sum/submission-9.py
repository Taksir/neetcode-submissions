class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        idx = 0
        ans = []

        for idx, n in enumerate(nums):
            if n > 0:
                break
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue

            l, r = idx + 1, len(nums) - 1
            target = -1 * nums[idx]
            

            while l < r:
                if target == nums[l] + nums[r]:
                    ans.append([nums[idx], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif target < nums[l] + nums[r]:
                    r -= 1
                else:
                    l += 1


        return ans