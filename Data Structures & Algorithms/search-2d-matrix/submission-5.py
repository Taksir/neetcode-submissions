class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        
        if l > r:
            return False
        
        row = mid
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            
        return False