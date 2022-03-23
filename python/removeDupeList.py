class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDupe(head):
    valToDelete = cur = head

    while cur:
        if valToDelete.val != cur.val:
            valToDelete.next = cur
            valToDelete = cur
        cur = cur.next

        if cur is None:
            valToDelete.next = cur
        return head
