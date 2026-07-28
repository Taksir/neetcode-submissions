import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = l + (r - l) // 2
            time = sum([math.ceil(p/mid) for p in piles])

            if time > h: # we slow. so we increase search range
                l = mid + 1
            else: # mid is a valid ans. but is the minimumest? so, we 
                  # search for even smaller valid ans by r = mid - 1
                res = mid
                r = mid - 1
        return res