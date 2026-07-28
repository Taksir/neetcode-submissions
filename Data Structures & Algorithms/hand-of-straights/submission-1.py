class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        nums = list(set(hand))
        nums.sort()
        freqs = collections.Counter(hand)
        pointer = 0
        while pointer < len(nums):
            val = nums[pointer]
            for i in range(groupSize):
                if val not in freqs or freqs[val] == 0:
                    return False
                freqs[val] -= 1
                val += 1
            while pointer < len(nums) and freqs[nums[pointer]] == 0:
                pointer += 1
            
        return True
