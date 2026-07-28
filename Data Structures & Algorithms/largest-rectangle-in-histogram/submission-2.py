class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                h = heights[index]
                leftIndex = stack[-1]
                width = i - leftIndex - 1
                maxArea = max(maxArea, h * width)
 
            stack.append(i)
        
        return maxArea