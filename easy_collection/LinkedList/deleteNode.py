# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next.next is not None:
            node.val = node.next.val
            node = node.next
        else:
            node.val = node.next.val
            node.next = None
