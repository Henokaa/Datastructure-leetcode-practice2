# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd = head
        even = None
        even_head = None
        if head.next:
            even = head.next
            even_head = even
        while odd.next and odd.next.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
    
        # print(head)
        # print(even_head)
        odd.next = even_head
        return head
            
     
                
        
        
            
        
        