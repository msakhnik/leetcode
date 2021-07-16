"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5


"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        sentinel = ListNode(0)
        sentinel.next = head
        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return sentinel.next


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(6)
node.next.next.next = ListNode(3)
node.next.next.next.next = ListNode(6)
node.next.next.next.next.next = ListNode(6)
node.next.next.next.next.next.next = ListNode(6)
some = Solution().removeElements(node, 6)
