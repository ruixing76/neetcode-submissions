class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        path=[]
        ans=[]
        # iterate subsets start from i
        def dfs(i):
            ans.append(path.copy())
            # choose j and make this as a new start
            for j in range(i,n):
                path.append(nums[j])
                dfs(j+1)
                path.pop()
        dfs(0)
        return ans