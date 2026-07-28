class Solution:
    def trap(self, height: List[int]) -> int:
        # get max. two subproblems; from left to max and right to max.
        # 2 pointers. if r < l, add water. else, l = r = that point
        maxVal = max(height)
        maxP = height.index(maxVal)

        l = r = 0
        water = 0

        while r <= maxP:
            if height[r] < height[l]:
                water += height[l] - height[r]
            else:
                l = r 
            r += 1

        l = r = len(height) - 1
        while l >= maxP:
            if height[l] < height[r]:
                water += height[r] - height[l]
            else:
                r = l 
            l -= 1

        return water