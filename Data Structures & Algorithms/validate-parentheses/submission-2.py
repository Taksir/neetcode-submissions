class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {'}' : '{', ']' : '[', ')' : '('}
        stack = []

        for ch in s:
            if ch in mapper:
                if not stack or stack.pop() != mapper[ch]:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0
            