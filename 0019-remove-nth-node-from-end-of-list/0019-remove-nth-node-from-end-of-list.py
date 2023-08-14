# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        tail = dummy
        remove = head
        for i in range(n):
            remove = remove.next
        
        
        while remove:
            tail = tail.next
            remove = remove.next
        
        tail.next = tail.next.next
        return dummy.next
        
        