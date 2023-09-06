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
        if not head:
            return None
        slow = head
        fast = head
        terminate = slow
        while fast and fast.next:
            terminate = slow
            slow = slow.next
            fast = fast.next.next
    
        first = None
        sec = slow
        third = slow.next
        # handle errors 
        
        while sec:
            sec.next = first
            first = sec
            sec = third
            if third:
                third = third.next
                
        terminate.next = None
        # print(first)
        # print(head)
        end = first
        start = head
        
        # first variable
        while start and end:
            temp1 = start.next
            temp2 = end.next
            start.next = end
            end.next = temp1
            last = end
            start = temp1
            end = temp2
        if end:
            last.next = end
        return head
            