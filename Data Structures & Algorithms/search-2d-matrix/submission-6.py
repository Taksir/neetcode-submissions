class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l < r:
            mid = l + (r - l) // 2
            if target <= matrix[mid][-1]:
                r = mid
            else:
                l = mid + 1
        if not(matrix[l][0] <= target <= matrix[l][-1]):
            return False 
        row = l

        l, r = 0, len(matrix[0]) - 1
        while l < r:
            mid = l + (r - l) // 2
            if target <= matrix[row][mid]:
                r = mid
            else:
                l = mid + 1

        return True if matrix[row][l] == target else False