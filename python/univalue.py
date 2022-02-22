'''
Write a function, is_univalue_list, that takes in the head of a linked list as an argument.
The function should return a boolean indicating whether or not the linked list contains exactly one unique value.

You may assume that the input list is non-empty
'''
def univalue(head):
    current = head
    while current is not None:
        if current.val != head.val:
            return False
        current = current.next

    return True
