class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        visited=[ [0 for _ in range(n)] for _ in range(m)]
        found=False
                
        def dfs(i,j,k):
            nonlocal found
            if 0<=i<m and 0<=j<n and visited[i][j]==0 and board[i][j]==word[k]:
                if k==len(word)-1:
                    return True
                visited[i][j]=1
                found = (dfs(i-1,j,k+1) 
                or dfs(i,j-1,k+1)
                or dfs(i,j+1,k+1)
                or dfs(i+1,j,k+1))
                visited[i][j]=0
                return found
            else:
                return False
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False