class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        heapq.heapify(hand) # O(n)
        freqs = collections.Counter(hand) # O(n)

        while hand: # O(n)
            val = heapq.heappop(hand)
            if freqs[val] == 0:
                continue
            for i in range(groupSize):
                if val not in freqs or freqs[val] == 0:
                    return False
                freqs[val] -= 1
                val += 1
            
        return True
                    



