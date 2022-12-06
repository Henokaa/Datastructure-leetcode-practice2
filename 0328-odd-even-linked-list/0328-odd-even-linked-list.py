# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        startodd = odd
        starteven = even
        r = 1
        cur = head
        while cur:
            # print(starteven)
            if r % 2 == 0:
                even.next = cur
                even = even.next
            else:
                odd.next = cur
                odd = odd.next
            
            cur = cur.next
            r += 1
        
        odd.next = starteven.next
        even.next = None
        
        return startodd.next
        
        