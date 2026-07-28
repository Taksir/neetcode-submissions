class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target > mid, target on right segment definitely
        # if equal return
        # else, if target < l, go to right segment, else left

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[l]  <= nums[mid]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         left, right = 0, n - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             # Case 1: find target
#             if nums[mid] == target:
#                 return mid
#             # Case 2: subarray on mids left is sorted
#             elif nums[mid] >= nums[left]:
#                 if target >= nums[left] and target < nums[mid]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             # Case 3: subarray on mid's right is sorted.
#             else:
#                 if target <= nums[right] and target > nums[mid]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#         return -1