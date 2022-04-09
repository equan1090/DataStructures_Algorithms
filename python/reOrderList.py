'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''

def reorderList(head):
    # Get mid of LinkedList
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    #reverse second half of linked list
    tmp = slow.next
    slow.next = None
    slow = tmp
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    l1, l2 = head, prev
    tail = head
    count = 0
    while prev:
        if count % 2 == 0:
            tail.next = l2
            l2 = l2.next
        else:
            tail.next = l1
            l1 = l1.next

