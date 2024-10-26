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
        n = len(nums)
        k %= n  # Handles cases where k > len(nums)

        # Separate into two lists
        store1 = nums[n - k:]  # Last k elements
        store2 = nums[:n - k]  # Elements before the last k elements

        # Combine the lists and write back to `nums` in place
        nums[:] = store1 + store2
        
        
            
        
        
        