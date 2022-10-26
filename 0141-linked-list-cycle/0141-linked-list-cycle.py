# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        firstCycle = True
        
        while fast and fast.next:
            if slow == fast and not firstCycle:
                return True
            slow = slow.next
            fast = fast.next.next
            firstCycle = False
        return False