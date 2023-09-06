# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        first = None
        sec = head
        third = head.next
        
        while sec:
            sec.next = first
            first = sec
            sec = third
            if third:
                third = third.next
            
        return first