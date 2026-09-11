class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_dict=defaultdict(int)
        for num in nums:
            hash_dict[num]+=1
        sorted_dict=sorted(hash_dict.items(),key=lambda x:x[1], reverse=True)
        result = [item[0] for item in sorted_dict[:k]]
        return result
