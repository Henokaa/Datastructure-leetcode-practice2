class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        '''
        dp take and not take
        check and append
        '''
        arr = []
        answer = []
        temp = []
        def dfs(i):
            if i == len(nums):
                if arr:
                    answer.append(arr.copy())
                return
            
            flag = 0
            for x in arr:
                if abs(x - nums[i]) == k:
                    flag = 1
                    break
                    
            if flag == 0:
                arr.append(nums[i])
                dfs(i+1)
                arr.pop()
                
            dfs(i+1)
        
        dfs(0)
        return len(answer)