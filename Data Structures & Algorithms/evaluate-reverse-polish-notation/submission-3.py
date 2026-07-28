class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for tok in tokens:
            if tok not in ['+', '-', '/', '*']:
                nums.append(int(tok))
            else:
                b = nums.pop()
                a = nums.pop()
                if tok == '+':
                    nums.append(a + b)
                elif tok == '-':
                    nums.append(a - b)
                elif tok == '*':
                    nums.append(a * b)
                else:
                    nums.append(int(a/b))
        return nums[0]