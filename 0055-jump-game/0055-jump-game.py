class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = len(nums) - 1
        goal = len(nums) - 1
        while r >= 0:
            if r + nums[r] >= goal:
                goal = r
            r -= 1
        
        print(goal)
        if goal == 0:
            return True
        else:
            return False
        
        

        