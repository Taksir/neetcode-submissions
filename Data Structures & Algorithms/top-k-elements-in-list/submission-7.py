
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for i in range(len(nums) + 1)]

        count = dict() # num2freq
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, freq in count.items():
            freqs[freq].append(n)

        print(freqs)
        res = []
        for i in range(len(freqs) - 1, -1, -1):
            for n in freqs[i]:
                res.append(n)
                if len(res) == k:
                    return res