class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]: # left half sorted
                if nums[mid] > target >= nums[l]:
                    r = mid
                else:
                    l = mid + 1
            else: # unsorted part
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        
        return l if nums[l] == target else -1