# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur_point = head
        prev_point = None
        while cur_point is not None:
            next_point = cur_point.next
            cur_point.next = prev_point
            prev_point = cur_point
            cur_point = next_point

        return prev_point
