class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        mincount = 0
        for i in range(len(nums)):
            if nums[i] in counter:
                counter[nums[i]] += 1
            else:
                counter[nums[i]] = 1
            mincount = max(mincount, counter[nums[i]])
        
        
        if mincount >= 2:
            return True
        else:
            return False
        