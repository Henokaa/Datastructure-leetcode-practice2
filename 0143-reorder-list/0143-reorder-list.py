# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head
        slow = head
        fast = head.next
        
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next 
            slow = slow.next
        
        
        prev = None
        cur = slow.next 
        slow.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur 
            cur = temp
        
        
        first = head
        sec = prev
        while sec:
            temp1 = first.next
            temp2 = sec.next
            first.next = sec
            sec.next = temp1
            sec = temp2
            first = temp1
        
        
        
            
            