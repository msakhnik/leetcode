"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        p1 = sentinel
        p2 = sentinel
        for _ in range(n + 1):
            p1 = p1.next

        while p1:
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next

        return sentinel.next


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
result_node = Solution().removeNthFromEnd(node, 2)
assert result_node.next.next.next.val == 5
