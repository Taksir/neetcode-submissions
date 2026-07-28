class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapper = {'2':'abc',
                  '3':'def',
                  '4':'ghi',
                  '5':'jkl',
                  '6':'mno',
                  '7':'pqrs',
                  '8':'tuv',
                  '9':'wxyz'}        
        ans = []
        combo = []
        def dfs(i):
            if i == len(digits):
                ans.append(''.join(combo))
                return
            
            for ch in mapper[digits[i]]:
                combo.append(ch)
                dfs(i + 1)
                combo.pop()
        if digits:
            dfs(0)
        return ans            