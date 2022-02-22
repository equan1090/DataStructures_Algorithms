'''
Write a function, longest_streak, that takes in the head of a linked list as an argument.
The function should return the length of the longest consecutive streak of the same value within the list.
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def longest_streak(head):
    prev = Node(None)
    maxStreak = 0
    currStreak = 0
    current = head
    while current is not None:
        if current.val == prev.val:
            currStreak += 1
        else:
            currStreak = 1

        if currStreak > maxStreak:
            maxStreak = currStreak

        prev = current
        current = current.next
    return maxStreak
