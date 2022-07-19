class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        
        res = 1
        for i in range(len(nums)):
            if i == 0:
                res *= nums[i] 
                continue
            answer[i] = res
            res *= nums[i]
        
        res = 1
        for j in range(len(nums)-1 , -1, -1):
            if j == len(nums) - 1:
                res *= nums[j]
                continue
            
            answer[j] *= res
            res *= nums[j]
        
        return answer
            