class Solution:
    def binary_search(self, nums: List[int], target:int, l:int, r:int) -> int:
        if l > r:
            return -1
        mid = l + (r-l)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(nums, target, l, mid-1)
        else:
            return self.binary_search(nums, target, mid+1, r)
        
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        return self.binary_search(nums, target, l, r)