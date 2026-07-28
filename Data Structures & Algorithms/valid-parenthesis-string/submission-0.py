class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmin, leftmax = 0, 0

        for ch in s:
            if ch == "(":
                leftmin, leftmax = leftmin + 1, leftmax + 1
            elif ch == ')':
                leftmin, leftmax = leftmin - 1, leftmax - 1
            else:
                leftmin, leftmax = leftmin - 1, leftmax + 1

            if leftmin < 0:
                leftmin = 0
            if leftmax < 0:
                return False

        return leftmin == 0
