class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        https://www.reddit.com/r/leetcode/comments/y7igv5/tanked_one_of_the_faang_interview_feel_miserable/
        '''  
        '''Bruteforce - for every number either take it or don't so 2 option for every n. 2^n
        dp - time complexity - o(n^2)'''
        
        '''
        this time complexity is - i * prev = nums.length * nums[i]
        '''
        memo = {}
        def dp(i):
            
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            
            value = 0
            temp1 = 0
            for x in range(i, len(nums)):
                if nums[x] > nums[i]:
                    value = 1 + dp(x)
                temp1 = max(temp1, value)
            
            memo[i] = temp1
            return temp1
            
        z = float('-inf')
        for i in range(len(nums)):
            temp = dp(i)
            z = max(z, temp + 1)
            # print(temp)
            
        print(memo)
        return z
    
        


