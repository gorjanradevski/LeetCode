# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/

from typing import List
from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        my_queue = Queue()
        my_queue.put(root)
        levels = []
        while not my_queue.empty():
            cur_size = my_queue.qsize()
            cur_level = []
            while cur_size > 0:
                elem = my_queue.get()
                cur_level.append(elem.val)
                cur_size -= 1
                if elem.left is not None:
                    my_queue.put(elem.left)
                if elem.right is not None:
                    my_queue.put(elem.right)
            levels.append(cur_level)
        return levels