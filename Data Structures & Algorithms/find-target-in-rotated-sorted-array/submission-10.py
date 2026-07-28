class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        if target <= nums[len(nums) - 1] and nums[l] <= target: 
            l, r = l, len(nums) - 1
        else:
            l, r = 0, l - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

            
        return -1