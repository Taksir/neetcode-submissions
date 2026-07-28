class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        top, bot = 0, len(matrix) - 1
        row = 0
        while top <= bot:
            mid = top + (bot - top) // 2
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                row = mid
                break
        
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
            
            
        