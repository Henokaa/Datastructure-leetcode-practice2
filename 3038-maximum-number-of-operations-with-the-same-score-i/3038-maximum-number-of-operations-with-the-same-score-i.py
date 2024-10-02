class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        '''
        <= 2 elements
        same
        '''
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            stack.append(nums[i])
        
        prev = float('inf')
        count = 0
        while len(stack) >= 2:
            num1 = stack.pop()
            num2 = stack.pop()
            
            total = num1 + num2
            if total != prev and prev != float('inf'):
                return count
            
            count += 1
            prev = total
            
        return count