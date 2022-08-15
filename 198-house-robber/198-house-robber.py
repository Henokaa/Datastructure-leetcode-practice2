class Solution:
    def rob(self, nums: List[int]) -> int:
        
                # empty case
        if not nums:
            return 0
        
        dp = [None for x in range(len(nums)+1)]
        # base case
        b = 0
        a = nums[len(nums)-1]
        
        for i in range(len(nums)-2, -1, -1):
            temp = max(a, b+nums[i])
            b = a
            a = temp
            
        
        return a
    
#     1,2,3,1
#     1,2,4,4
    
#     2,1,1,2
#     2,2,3,4