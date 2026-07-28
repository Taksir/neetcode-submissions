class Solution:
    def trap(self, height: List[int]) -> int:
        maxIdx = height.index(max(height))
        water = 0
        # first loop from left
        l, r = 0, 0

        while r <= maxIdx:
            if height[r] < height[l]:
                water += height[l] - height[r]
            else:
                l = r
            r += 1

        # second loop from right
        l, r = len(height) - 1, len(height) - 1

        while l >= maxIdx:
            if height[l] < height[r]:
                water += height[r] - height[l]
            else:
                r = l
            l -= 1
        
        return water