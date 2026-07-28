class Solution:
    def trap(self, height: List[int]) -> int:
        maxH = max(height)
        maxIdx = height.index(maxH)

        l = r = 0
        water = 0

        while r <= maxIdx:
            if height[r] < height[l]:
                water += (height[l] - height[r])
            else:
                l = r
            r += 1

        l = r = len(height) - 1

        while l >= maxIdx:
            if height[l] < height[r]:
                water += (height[r] - height[l])
            else:
                r = l
            l -= 1

        return water