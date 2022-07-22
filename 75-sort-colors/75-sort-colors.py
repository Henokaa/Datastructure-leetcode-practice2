class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        print(count)
        def inplace(x,y):
            for i in range(y):
                nums[self.pos+i] = x
            self.pos += i+1
        self.pos = 0
        if 0 in count:
            inplace(0,count[0])
        if 1 in count:
            inplace(1,count[1])
        if 2 in count:
            inplace(2,count[2])
                
       
                
        