# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        slow = head
        fast = head.next
        
        while fast:
            fast = fast.next
            if fast is not None:
                fast = fast.next
            slow = slow.next
        
        return slow
        