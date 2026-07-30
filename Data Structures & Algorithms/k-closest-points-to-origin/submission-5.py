import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return x ** 2 + y ** 2

        newp = [(-dist(x,y), x, y) for x, y in points]
        heapq.heapify(newp)

        while len(newp) > k:
            heapq.heappop(newp) 

        ans = []
        while newp:
            _, x, y = heapq.heappop(newp)
            ans.append([x, y])

        return ans