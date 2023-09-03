class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        index
        [1,3,4,2,2]
        [0,1,2,3,4]
         ^
        think of the numbers as index and point to them if they depeat we have a cycle
        1->3->2->4->2
        
        Floyd cycle detection
        
        1) first intersect fast and slow
        2) then start from the begining pointer P and start moving slow until they intersect
                    
            
        '''
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        print(fast, slow)
        start = 0
        while True:
            start = nums[start]
            slow = nums[slow]
            if start == slow:
                return start
            
        '''
        
        Floyd cycle detection - if the fast pointer catches up to the slow pointer, it means there is a cycle in the linked list. If the fast pointer reaches the end of the list without catching up, it means the list is acyclic. Then the distance between where they catch up and where the start with give you the inital point
        '''
            
            