'''
Write a function, zipper_lists, that takes in the head of two linked lists as arguments.
The function should zipper the two lists together into single linked list by alternating nodes.
If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes.
The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty.
'''

def zipper_lists(head_1, head_2):
    tail = head_1
    current1 = head_1.next
    current2 = head_2
    count = 0

    while current1 is not None and current2 is not None:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next

        tail = tail.next
        count += 1
    if current1 is None:
        tail.next = current2
    if current2 is None:
        tail.next = current1
    return head_1

