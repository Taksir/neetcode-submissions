class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1

        while t <= b:
            mid = t + (b - t) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif target < matrix[mid][0]:
                b = mid - 1
            else:
                t = mid + 1
            
        l, r = 0, len(matrix[mid]) - 1

        while l <= r:
            m = l + (r - l) // 2
            if target == matrix[mid][m]:
                return True
            elif target < matrix[mid][m]:
                r = m - 1
            else:
                l = m + 1
        
        return False