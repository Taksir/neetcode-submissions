from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for _ in range(len(nums) + 1)]
        counts = Counter(nums)
        for n, freq in counts.items():
            freqs[freq].append(n)
        ans = []
        for r in range(len(freqs) - 1, -1, -1):
            if k == 0:
                break
            if freqs[r]:
                for n in freqs[r]:
                    ans.append(n)
                    k -= 1
                    if k == 0:
                        break
        return ans