class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m=len(grid)
        n=len(grid[0])

        def inArea(i,j):
            if 0<=i<m and 0<=j<n and grid[i][j]=="1":
                return True
            else:
                return False
        
        def dfs(i,j):
            if inArea(i,j):
                grid[i][j]="2"
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
            else:
                return

        ans=0
        for i in range(m):
            for j in range(n):
                if inArea(i,j):
                    dfs(i,j)
                    ans+=1
        return ans