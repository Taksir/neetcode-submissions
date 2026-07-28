class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        ans = [0] * len(temp)
        stack = []

        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                day = stack.pop()
                ans[day] = i - day

            stack.append(i)

        return ans