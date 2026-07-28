class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        ans = [0] * len(t)
        stack = []
        for i, temp in enumerate(t):
            while stack and temp > t[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx

            stack.append(i)

        return ans