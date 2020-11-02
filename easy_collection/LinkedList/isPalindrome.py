# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ordinary = []
        total = 0
        while head is not None:
            ordinary.append(head.val)
            total += 1
            head = head.next
        for i in range(total // 2):
            if ordinary[i] != ordinary[-(i + 1)]:
                return False
        return True