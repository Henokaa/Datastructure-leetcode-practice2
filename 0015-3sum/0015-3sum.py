class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        understand
            
        [-1,0,1,2,-1,-4]
        -1 
        [-4,-1,-1,0,1,2]
          ^ 
        pick a number
            two pointer search
            
        naive 
        
        optimal
        
        edge cases
        
        '''
        nums.sort()
        answer = set() # attention
        for i in range(len(nums)):
            number = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                # print(l,r)
                if nums[l] + nums[r] == number:
                    answer.add((nums[i], nums[l], nums[r]))  # []
                    l += 1 # l += 1
                    r -= 1 # r -= 1
                
                elif nums[l] + nums[r] > number:
                    r -= 1
                
                else:
                    l += 1
        
        print(answer)
        return list(answer)
                    