class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        path=[]
        def dfs(i, left):
            if left==0:
                ans.append(path.copy())
                return
            for j in range(i,len(nums)):
                if nums[j]>left:
                    break
                path.append(nums[j])
                dfs(j,left-nums[j])
                path.pop()
        dfs(0,target)
        return ans