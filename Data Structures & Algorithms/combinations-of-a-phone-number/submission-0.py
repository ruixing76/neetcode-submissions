MAPPING=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n=len(digits)
        path=[]
        ans=[]
        if n==0:
            return ans
        def dfs(i):
            if i ==n:
                ans.append("".join(path))
                return
            for c in MAPPING[int(digits[i])]:
                path.append(c)
                dfs(i+1)
                path.pop()
        dfs(0)
        return ans