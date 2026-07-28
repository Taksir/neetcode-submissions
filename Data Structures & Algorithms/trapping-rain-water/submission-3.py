class Solution:
    def trap(self, height: List[int]) -> int:
        idx = height.index(max(height))
        water = 0
        l, r = 0, 0
        while r <= idx:
            if height[r] < height[l]:
                water += height[l] - height[r]
            else:
                l = r
            r += 1
        
        l, r = len(height) - 1, len(height) - 1
        while l >= idx:
            if height[l] < height[r]:
                water += height[r] - height[l]
            else:
                r = l
            l -= 1

        return water