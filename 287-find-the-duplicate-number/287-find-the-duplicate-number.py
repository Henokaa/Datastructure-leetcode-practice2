class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        index
        [1,3,4,2,2]
         ^
        think of the numbers as index and point to them if they depeat we have a cycle
        1->3->2->4->2
        
        '''
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
         
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            
            