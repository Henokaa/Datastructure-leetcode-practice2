# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        cur = dummy
        for i in range(n):
            cur = cur.next
            
        # print(cur)
        
        prev = dummy
        
        
        while cur.next:
            cur = cur.next
            prev = prev.next
        
        prev.next = prev.next.next
        return dummy.next
        