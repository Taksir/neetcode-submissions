# from math import ceil
# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         for i in range(1, max(piles) + 1):
#             time = 0
#             for pile in piles:
#                 time += ceil(pile/i)
#             print(i, time)
#             if time < h:
#                 break
#         return i


# piles = [25,10,23,4], h = 4
# t =  62 62 23 .... 7 6 6 6 5 5 .. 4
# we are searching in something sorted from large to small

from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # remember the ranges, especially max
        res = 0
        while l <= r:
            mid = l + (r-l) // 2
            # time = 0
            # for i in range(len(piles)):
            #     time += ceil(piles[i] / mid)
            time = sum(math.ceil(piles[i] / mid) for i in range(len(piles)))
            if time > h:
                l = mid + 1
            else:   # if time <= h, we just went immediately smaller than h. this is the answer.
                res = mid
                r = mid - 1
        
        return res
