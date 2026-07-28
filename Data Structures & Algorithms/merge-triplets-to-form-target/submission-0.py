class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        new = [float('-inf')] * 3
        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            for i in range(3):
                new[i] = max(new[i], trip[i])
        return new == target
            