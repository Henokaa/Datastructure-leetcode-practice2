class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        
        [1,2,3,4,5,6,7]
        
        
        constraint 
        
        naive 
            from k to end
                append
            
            from 0 to k
                append
                
            
        
        optimal
        
        edges
        
        
        '''
        
        p1 = (len(nums)) - k % len(nums)
        # print(p1)
        store_p1 = p1
        store1 = []
        while p1 < len(nums):
            store1.append(nums[p1])
            p1 += 1
        
        # print(store1)
        
        p2 = 0
        store2 = []
        while p2 < store_p1:
            store2.append(nums[p2])
            p2 += 1
        
        # print(store2)
        
        # for i in range(len(store2)):
        #     store1.append(store2[i])
            
        nums[:] = store1 + store2
        
        
            
        
        
        