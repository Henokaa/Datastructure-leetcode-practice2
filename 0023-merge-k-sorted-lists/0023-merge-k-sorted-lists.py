# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists = []
            l = 0
            r = 1
            while r < len(lists):
                l1 = lists[l]
                l2 = lists[r]
                temp = self.mergeList(l1,l2)
                mergedLists.append(temp)
                l += 2
                r += 2
            
            if l < len(lists) and lists[l]:
                mergedLists.append(lists[l])
            
            lists = mergedLists
        return lists[0]
            
            # for i in range(0, len(lists), 2):
            #     l1 = lists[i]
            #     l2 = lists[i + 1] if (i + 1) < len(lists) else None
            #     mergedLists.append(self.mergeList(l1, l2))
            #     # print(mergedLists)
            # lists = mergedLists
            
        # return lists[0]
    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        # print(dummy.next)
        return dummy.next