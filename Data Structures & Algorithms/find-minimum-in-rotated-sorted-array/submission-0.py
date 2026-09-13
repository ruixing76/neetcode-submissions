class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force
        min_val=1001
        for num in nums:
            min_val=min(min_val,num)
        return min_val
        
