# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(next=head)
        first = dummy
        second = dummy
        for _ in range(n + 1):
            second = second.next
        while second.next is not None:
            first = first.next
            second = second.next
        first.next = first.next.next

        return dummy.next