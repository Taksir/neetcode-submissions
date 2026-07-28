class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        maxArea = 0
        stack = []
        r = 0

        while r < len(heights):
            while stack and heights[stack[-1]] > heights[r]:
                idx = stack.pop()
                h = heights[idx]
                left_idx = stack[-1]
                width = r - left_idx - 1
                maxArea = max(maxArea, h * width)
                
            stack.append(r)
            r += 1

        return maxArea