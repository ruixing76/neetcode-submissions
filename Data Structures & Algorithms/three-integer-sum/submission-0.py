class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        nums.sort()
        # iterate each i, then the left sum would be 0-nums[i]
        # use two pointers to add up to this sum, if smaller, move left, otherwise move right
        # avoid duplicates by checking if left has met before (we will get the same answer for this one)
        ans=[]
        for i,num in enumerate(nums):
            if num>0:
                break
            if i>0 and num==nums[i-1]:
                continue
            left_sum=0-num
            j,k=i+1,len(nums)-1
            while j<k:
                cur_sum=nums[j]+nums[k]
                if cur_sum==left_sum:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                elif cur_sum<left_sum:
                    j+=1
                else:
                    k-=1
        return ans