import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            mid = l + (r - l) // 2
            total_time = sum([math.ceil(piles[i] / mid) for i in range(len(piles))])

            if total_time <= h:
                r = mid
            else:
                l = mid + 1
        
        return l