class Solution:
    def isHappy(self, n: int) -> bool:
        record=set()
        def compute(k):
            part_ans=0
            while k>0:
                root=(k%10)
                part_ans+=root*root
                k//=10
            return part_ans
        while n!=1 and n not in record:
            record.add(n)
            n=compute(n)
        return n==1