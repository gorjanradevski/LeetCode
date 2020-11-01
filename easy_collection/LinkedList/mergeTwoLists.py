# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_node = ListNode(0)
        iter_dummy = dummy_node
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                iter_dummy.next = l1
                l1 = l1.next
            else:
                iter_dummy.next = l2
                l2 = l2.next
            iter_dummy = iter_dummy.next
        else:
            iter_dummy.next = l2 if l1 is None else l1

        return dummy_node.next
