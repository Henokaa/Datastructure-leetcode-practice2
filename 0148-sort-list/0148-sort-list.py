# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
    
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, list1,list2):
        dummy = ListNode()
        dum_head = dummy
        first = list1
        sec = list2
        
        while first and sec:
            if first.val <= sec.val:
                dummy.next = first
                first = first.next
            else:
                dummy.next = sec
                sec = sec.next
            dummy = dummy.next
        
        if first:
            dummy.next = first
        
        if sec:
            dummy.next = sec

        return dum_head.next