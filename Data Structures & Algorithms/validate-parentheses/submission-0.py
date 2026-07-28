class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'}' : '{', ')' : '(', ']' : '['}
        stack = []

        for ch in s:
            if ch in brackets and stack:
                if stack.pop() != brackets[ch]:
                    return False
            else:
                stack.append(ch)

        return not stack