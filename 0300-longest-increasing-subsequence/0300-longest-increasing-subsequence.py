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
        length = len(nums)
        dp = [0] * len(nums)
        
        dp[length-1] = 1
        ans = 1
        for i in range(len(nums)-2, -1, -1):
            temp = 1
            for j in range(i + 1, length):
                # print(i,j)
                if nums[i] < nums[j]:
                    temp = max(temp, 1 + dp[j])
            dp[i]= temp 
            ans = max(temp, ans)
        # print(dp)
        return ans
                
            
                
            
    
        


