import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = float('inf')
        while l <= r:
            mid = l + (r - l) // 2
            time = sum([math.ceil(p/mid) for p in piles])

            if time > h: # we slow. so we increase search range
                l = mid + 1
            else: # 
                res = min(res, mid)
                r = mid - 1
        return res