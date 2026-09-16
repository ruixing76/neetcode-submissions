class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = 2*n
        ans=[]
        path=['']*m

        def dfs(i,n_left):
            if i==m:
                ans.append("".join(path))
                return ans
            # n_left means the count of left parentheses
            # the count of right parentheses is i-n_left
            if i-n_left<n_left:
                path[i]=(')')
                dfs(i+1,n_left)
            if n_left<n:
                path[i]=('(')
                dfs(i+1,n_left+1)
        dfs(0,0)
        return ans