class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        ans = []
        for i in range(len(nums)):
            nums[i] = nums[i] **2
        # print(nums)
        while l <= r:
            # print(l,r)
            if nums[l] >= nums[r]:
                ans.append(nums[l])
                l += 1
                
            
            elif nums[r] > nums[l]:
                ans.append(nums[r])
                r -= 1
        
        return ans[::-1]
        
                
        