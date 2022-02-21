class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists(head_1, head_2):
    dummyNode = Node(None)
    tail = dummyNode
    current1 = head_1
    current2 = head_2

    while current1 is not None and current2 is not None:
        if current1.val < current2.val:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next

    if current1 is None:
        tail.next = current2
    if current2 is None:
        tail.next = current1
    return dummyNode.next
