"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{}->{}".format(self.val, self.next)


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head

        def helper(node):
            """
            Reverse k and return new_head
            """
            new_head = head
            target = 1
            end = head
            while target < k:
                current = head.next
                head.next = current.next
                current.next = new_head
                new_head = current
                target += 1
            return new_head

        ptr = head
        ktail = None
        new_head = None
        while ptr:
            count = 0
            ptr = head
            while count < k and ptr:
                ptr = ptr.next
                count += 1
            if count == k:
                revHead = helper(head)
                if not new_head:
                    new_head = revHead
                if ktail:
                    ktail.next = revHead

                ktail = head
                head = ptr

        if ktail:
            ktail.next = head

        return new_head if new_head else head


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
result = Solution().reverseKGroup(node, 2)

assert result.val == 2
assert result.next.val == 1
assert result.next.next.val == 4
assert result.next.next.next.val == 3
assert result.next.next.next.next.val == 5
