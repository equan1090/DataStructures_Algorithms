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
        
        left = head
        right = prev
        
        while left and right:
            # 1 -> 2 -> 3
            # 5 -> 4
            tmpLeft = left.next
            tmpRight = right.next
            left.next = right
            left = tmpLeft
            right.next = left
            right = tmpRight
        return head