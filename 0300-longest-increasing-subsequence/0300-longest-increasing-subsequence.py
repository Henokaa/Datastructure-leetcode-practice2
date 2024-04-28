class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        nums = [10,9,2,5,3,7,101,18]
        
        self.answer = 0
        def dfs(i, k):
            self.answer = max(self.answer, k)
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dfs(j, k+1)
            
            
        for i in range(len(nums)):
            dfs(i, 1)
        
        return self.answer
        '''
        self.answer = 0
        memo = {}
        def dfs(i):
            value = 1
            if i in memo:
                return memo[i]
            
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    node = 1 + dfs(j)
                    value = max(value, node)
            
            self.answer = max(self.answer, value)
            # print(value)
            memo[i] = value
            return value
                
            
            
        for i in range(len(nums)):
            result = dfs(i)
            # print(result)
        
        return self.answer