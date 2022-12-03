# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode()
        res = new
        rem = 0
        
        while l1 or l2 or rem:
            if not l1:
                val1 = 0
            if l1:
                val1 = l1.val
            if not l2:
                val2 = 0
            if l2:
                val2 = l2.val
            total = val1 + val2 + rem
            rem = total // 10
            value = total % 10
            new.next = ListNode(value)
            new = new.next
            if l1:
                l1 = l1.next
            if not l1:
                l1 = None
                
            
            
            if l2:
                l2 = l2.next
            if not l2 :
                l2  = None
                
            
     
      
        return res.next