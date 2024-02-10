class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_num = {}
        for i, x in enumerate(nums):
            sorted_num[i] = x
        
        sorted_tuple = sorted(sorted_num.items(), key=lambda x:x[1])
        
        # print(sorted_tuple)
        l = 0
        r = len(nums) - 1
        
        while l < r:
            if sorted_tuple[l][1] + sorted_tuple[r][1] == target:
                return [sorted_tuple[l][0],sorted_tuple[r][0]]
            elif sorted_tuple[l][1] + sorted_tuple[r][1] > target:
                r -= 1
            elif sorted_tuple[l][1] + sorted_tuple[r][1] < target:
                l += 1
        
        return [-1,-1]