class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction=[(-1,0),(+1,0),(0,-1),(0,+1)]
        if not grid or not grid[0]:
            return 0
        m=len(grid)
        n=len(grid[0])
        time=0
        q=deque()
        # locate the first rotten fruit
        fresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j]==1:
                    fresh+=1

        def valid(i,j):
            if 0<=i<m and 0<=j<n and grid[i][j]==1:
                return True
            else:
                return False
        while q and fresh>0:
            for _ in range(len(q)):
                i,j=q.popleft()
                for di,dj in direction:
                    ni=i+di
                    nj=j+dj
                    if valid(ni,nj):
                        q.append((ni,nj))
                        grid[ni][nj]=2
                        fresh-=1
            time+=1
        if fresh==0:
            return time
        else:
            return -1