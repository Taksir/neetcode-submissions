import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = ""
        while l <= r:
            mid = l + (r - l) // 2
            time = sum([math.ceil(p/mid) for p in piles])
            if time <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans