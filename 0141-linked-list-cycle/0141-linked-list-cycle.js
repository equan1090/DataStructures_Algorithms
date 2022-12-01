/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
const hasCycle = head => {
  while (head) {
    if (head.val === 'done') return true;

    head.val = 'done';
    head= head.next;
  }

  return false;
};
  