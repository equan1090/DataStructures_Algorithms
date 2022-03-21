'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer. Internally, pos is used to denote the index of the node
that tail's next pointer is connected to. Note that pos is not passed as a parameter.
'''
# Two pointer solution, fast and slow
#O(n) time | O(1) Space
def hasCycle(head):
    if not head:
        return False
    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


# Hash table solution
# O(n) time | O(n) space

# def hasCycle(head):
#     hsh = {}

#     while head:
#         if head in hsh:
#             return True
#         hsh[head] = True
#         head = head.next
#     return False
