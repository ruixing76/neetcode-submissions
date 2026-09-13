class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        ans=0
        streak=0
        for num in nums:
            if num-1 not in numSet:
                streak=0
                while num+streak in numSet:
                    streak+=1
                ans=max(ans,streak)
        return ans
            