
'''
Given the head of a singly linked list, return true if it is a palindrome.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    slow = fast = head
    # Get the middle of the linked list
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reverse linked list from mid to end
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    #check reversed with head
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True
