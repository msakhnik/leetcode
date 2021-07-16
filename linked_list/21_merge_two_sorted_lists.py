import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = tmp = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next

        if l1 is None:
            tmp.next = l2
        else:
            tmp.next = l1
        return sentinel.next


node1 = ListNode(1)
node1.next = ListNode(2)
node1.next.next = ListNode(4)

node2 = ListNode(1)
node2.next = ListNode(3)
node2.next.next = ListNode(4)

sol = Solution()
result = sol.mergeTwoLists(node1, node2)

assert result.val == 1
assert result.next.val == 1
