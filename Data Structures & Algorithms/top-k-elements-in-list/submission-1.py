class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        bucket=[[] for i in range(len(nums)+1)]
        for num in nums:
            count[num]+=1
        for num,cnt in count.items():
            bucket[cnt].append(num)
        ans=[]
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans)==k:
                    return ans
