class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_dict=defaultdict(int)
        for num in nums:
            hash_dict[num]+=1
        for each in hash_dict:
            if hash_dict[each]>1:
                return True
        return False