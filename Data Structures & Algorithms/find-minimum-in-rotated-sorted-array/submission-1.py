class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ans = float('infinity')
        while l <= r:
            if nums[l] < nums[r]:
                return min(ans, nums[l])
            mid = l + (r - l) // 2
            ans = min(ans, nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return ans
            

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         # two segments. either l and mid are in one, or mid and r in one.
#         # if nums[mid] >= nums[r], smallest is on right
#         # else smallest is on left
#         l, r = 0, len(nums) - 1
#         res = float('infinity')
#         while l <= r:
#             if nums[l] < nums[r]: # this means our window is sorted. we can return
#                 return min(res, nums[l])

#             mid = l + (r-l) // 2
#             res = min(res, nums[mid]) # always update the minimum here

#             if nums[mid] > nums[r]:
#                 l = mid + 1
#             else:
#                 r = mid - 1

#         return res