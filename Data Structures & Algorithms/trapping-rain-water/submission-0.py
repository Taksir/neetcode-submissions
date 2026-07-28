class Solution:
    def trap(self, height: List[int]) -> int:
        maxIdx = height.index(max(height))
        l = curIdx = curWater = 0
        ans = 0
        while curIdx <= maxIdx:
            if height[curIdx] < height[l]:
                curWater += (height[l] - height[curIdx])
            elif height[curIdx] > height[l]:
                ans += curWater
                curWater = 0
                l = curIdx
            curIdx += 1
        ans += curWater

        r = curIdx = len(height) - 1
        curWater = 0
        while curIdx >= maxIdx:
            if height[curIdx] < height[r]:
                curWater += (height[r] - height[curIdx])
            elif height[curIdx] > height[r]:
                ans += curWater
                curWater = 0
                r = curIdx
            curIdx -= 1
        ans += curWater

        return ans