# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/

from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        my_queue = Queue()
        my_queue.put(root)

        while not my_queue.empty():
            cur_size = my_queue.qsize()
            cur_level = []
            while cur_size > 0:
                elem = my_queue.get()
                cur_level.append(elem.val if elem is not None else None)
                cur_size -= 1
                if elem is not None:
                    my_queue.put(elem.left)
                    my_queue.put(elem.right)

            for i in range(len(cur_level)//2):
                if cur_level[i] != cur_level[-(i + 1)]:
                    return False
        return True
