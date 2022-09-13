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
        
        '''
        [3 10]
        
        1 -> 2 -> 3 -> 4 -> 5 -> 6
             |
             7 -> 8 -> 9 -> 10
                  |
                  11 -> 12
                  
        dummy - 1 - 2 - 7 - 8 - 11 - 12 - 10
                                      t
        '''
        

            
        #     cur.next = tmp
        #     tmp.prev = cur
        #     tmp.child = None
        #     cur = tmp
        # dummy.next.prev = None
        # return dummy.next