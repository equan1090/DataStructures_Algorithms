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
        if not head:
            return None
        
        self.dfs(head)
        return head
    
    
    def dfs(self, cur):
        while cur:
            nxt = cur.next
            if not nxt:
                tail = cur
            
            if cur.child:
                cur.child.prev = cur
                cur.next = cur.child
                child_tail = self.dfs(cur.child)
                
                if nxt:
                    nxt.prev = child_tail
                child_tail.next = nxt
                cur.child = None
            cur = cur.next
        return tail