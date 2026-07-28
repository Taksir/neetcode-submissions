class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first, second = 1, 2
        for i in range(n-2):
            temp = first + second
            first, second = second, temp

        return second