class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, nums[0]
        for i in range(1, len(nums)):
            temp = max(a + nums[i], b)
            a = b
            b = temp
        
        return b
    
#     1,2,3,1
#     1,2,4,4
    
#     2,1,1,2
#     2,2,3,4
# a=0, b=2, temp for the new one
