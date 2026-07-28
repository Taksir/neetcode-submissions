class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1


        sortedCount = sorted(count.items(), key = lambda item:item[1], reverse = True)
        
        x = 0
        ans = []
        while x < k:
            ans.append(sortedCount[x][0])
            x += 1

        return ans