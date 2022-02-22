'''
Write a function, add_lists, that takes in the head of two linked lists, each representing a number.
The nodes of the linked lists contain digits as values. The nodes in the input lists are reversed;
this means that the least significant digit of the number is the head.
The function should return the head of a new linked listed representing the sum of the input lists.
The output list should have its digits reversed as well.
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def add_lists(head_1, head_2):
    carry = 0
    dummy = Node(None)
    tail = dummy

    while head_1 or head_2 or carry:
        if head_1:
            carry += head_1.val
            head_1 = head_1.next
        if head_2:
            carry += head_2.val
            head_2 = head_2.next

        tail.next = Node(carry % 10)
        tail = tail.next
        carry //= 10
    return dummy.next
