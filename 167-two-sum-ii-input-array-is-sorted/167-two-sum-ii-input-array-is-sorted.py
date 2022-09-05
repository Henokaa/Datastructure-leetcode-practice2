class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        checker = {}
        r = 0
        while r < len(numbers):
            temp = target - numbers[r]
            if  temp in checker:
                return [checker[temp]+1, r+1]
            else:
                checker[numbers[r]] = r
                r += 1
        
'''
submisson one more optimal interms of space complexity 0(1)
'''