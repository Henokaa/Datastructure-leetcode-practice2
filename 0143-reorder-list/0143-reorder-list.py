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
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # print(slow.val)
        
        # reversing
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
        # print(first, prev)
        while first and sec:
            temp1 = first.next
            first.next = sec
            first = temp1
            temp2 = sec.next
            sec.next = first
            sec = temp2
            
            
        
        
            
            