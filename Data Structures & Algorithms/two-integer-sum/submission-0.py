class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        hash_dict=defaultdict(int)
        for i, num in enumerate(nums):
            if target-num in hash_dict:
                ans.append(hash_dict[target-num])
                ans.append(i)
            hash_dict[num]=i
        return ans