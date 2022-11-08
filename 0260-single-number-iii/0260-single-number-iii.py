class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans=0
        for item in nums:
            ans=ans^item
        t=ans
        count=0
        while(t):
            if t&1==1:
                break
            count+=1
            t=t>>1
        b=ans
        for item in nums:
            if (item>>count)&1==1:
                b=b^item
        return [b,ans^b]
        