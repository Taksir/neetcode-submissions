class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        nums = list(set(hand))
        nums.sort()
        freqs = collections.Counter(hand)

        while nums:
            val = nums[0]
            for i in range(groupSize):
                if val not in freqs:
                    return False
                freqs[val] -= 1
                if not freqs[val]:            
                    nums.remove(val)
                val += 1
            
        return True
