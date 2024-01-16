class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        number = sorted(nums)
        # print(number)
        count = 0
        for i in range(len(number)):
            if i - 1 >=0:
                if number[i-1] >= number[i]:
                    count += number[i-1] - number[i] + 1
                    number[i] = number[i] + number[i-1] - number[i] + 1
                    
        
        return count