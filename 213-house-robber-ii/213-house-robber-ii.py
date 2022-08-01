class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(nums):
            a , b = 0, nums[0]
            i = 1
            while i <= len(nums)-1:
                temp = max(a+nums[i], b)
                a = b
                b = temp
                i += 1 
                
            return b
        
        if len(nums) >= 2:
            value1 = helper(nums[:-1])
            value2 = helper(nums[1:])
            return max(value1, value2)
        else:
            return nums[0]
        
    
            
# [2, 3, 2]
# 2,3
# [3, 2]
# 3, 3
