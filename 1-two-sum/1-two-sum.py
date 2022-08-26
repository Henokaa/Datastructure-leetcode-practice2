class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two pass o(n)
        checker = {} # it couldn't set because there is duplicates in the array and they can be an answer
        for i in range(len(nums)):
            checker[nums[i]] = i
        
        for i in range(len(nums)):
            res = target - nums[i] 
            if res in checker and checker[res] != i:
                return [i, checker[res]]
        return []
                        
                