class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        ans = set()
        for i in range(len(nums)):
            dict_[nums[i]] = i
        
        for j in range(len(nums)):
            temp = target - nums[j]
            if temp in dict_:
                for x,y in dict_.items():
                    if temp == x and j != y:
                        ans.add(j)
                        ans.add(y)
                        
        return ans
                        
                