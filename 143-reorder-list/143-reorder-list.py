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
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next
        slow.next = None
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        
        left, right = head, prev
        
        # 1 2
        # 3 4
        
        
        # 1 2 3
        # 4 5
        while left and right:
            tmpL = left.next
            tmpR = right.next
            left.next = right
            left = tmpL
            right.next = left
            right = tmpR
            
            