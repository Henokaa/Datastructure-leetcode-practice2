class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        m = n + 1
        nums = [True] * n
        nums[0] = False
        nums[1] = False
        value = 0
        x = sqrt(n)
        for i in range(2,n):
            if i > x:
                break
            if nums[i] == True:
                value = i
                value += i
                while value < n:
                    nums[value] = False
                    value += i
                value = 0
            
        # print(nums)
        count = 0
        for i in range(len(nums)):
            if nums[i] == True:
                count += 1
                
        return count