"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return head
        
        dummy = Node(None)
        tail = dummy
        stack = [head]
        
        while stack:
            cur = stack.pop()
            if cur.next:
                stack.append(cur.next)
            if cur.child:
                stack.append(cur.child)
            
            tail.next = cur
            cur.prev = tail
            cur.child = None
            tail = cur
        dummy.next.prev = None
        return dummy.next
        
        
