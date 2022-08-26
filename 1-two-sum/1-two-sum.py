class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # one pass o(n)
        checker = {} # it couldn't set because there is duplicates in the array and they can be an answer
        
        for i in range(len(nums)):
            res = target - nums[i] 
            if res in checker:
                return [i, checker[res]]
            else:
                checker[nums[i]] = i
        return []
                        
                