class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        left = 0
        leftc = 0
        right = sum(nums)
        rightc = len(nums)
        
        best = 10 ** 20
        bestindex = -1
        
        for x in nums:
            left += x
            leftc += 1
            
            right -= x
            rightc -= 1
            
            if rightc == 0:
                rightc = 1
                
            score = abs(left // leftc - right// rightc)
            
            if score < best:
                best = score
                bestindex = leftc - 1
            
        return bestindex
        