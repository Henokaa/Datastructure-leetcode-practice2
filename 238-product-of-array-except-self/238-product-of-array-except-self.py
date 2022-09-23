class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [1,2,3,4]
        [24 , 24, 12,4]
        [1  ,  2, 6, 24]
        '''
        preFix = []
        preSum = 1
        for i in range(len(nums)):
            preSum *= nums[i]
            preFix.append(preSum)
    
        
        postFix = []
        postSum = 1
        for i in range(len(nums) - 1, -1, -1):
            postSum *= nums[i]
            postFix.append(postSum)
        
        postFix = postFix[::-1]
        ans = []
        print(postFix)
        temp = 1
        for i in range(len(nums)):
            if i - 1 >= 0:
                temp *= preFix[i-1]
            if i+1 < len(nums):
                temp *= postFix[i + 1]
            ans.append(temp)
            temp = 1
        
        return ans