"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{}->{}".format(self.val, self.next)


class Solution(object):
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        new_head = head
        while head.next is not None:
            current = head.next
            head.next = current.next
            current.next = new_head
            new_head = current
        return new_head


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
result = Solution().reverseList(node)
assert result.val == 5
assert result.next.val == 4
assert result.next.next.val == 3
assert result.next.next.next.val == 2
assert result.next.next.next.next.val == 1
assert result.next.next.next.next.next is None
