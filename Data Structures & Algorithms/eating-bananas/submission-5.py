import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = l + (r-l) // 2

            t = 0
            # for i in range(len(piles)):
            #     t += math.ceil(piles[i] / k)
            t = sum(math.ceil(piles[i] / k) for i in range(len(piles)))
            if t <= h:
                r = k - 1
                res = k
            else:
                l = k + 1
            
        return res
        
                