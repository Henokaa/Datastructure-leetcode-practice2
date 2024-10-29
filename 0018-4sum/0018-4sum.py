class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        sort()
        
        for 
            for 
                two pointers
            
        '''
        
        nums.sort()
        answer = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] + nums[i] + nums[j] == target:
                        answer.add(tuple([nums[l], nums[r], nums[i], nums[j]]))
                        l += 1
                        r -= 1
                        
                    
                    elif nums[l] + nums[r] + nums[i] + nums[j] < target:
                        l += 1
                    
                    elif nums[l] + nums[r] + nums[i] + nums[j] > target:
                        r -= 1
            
        return list(answer)