# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/

from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        my_queue = Queue()
        my_queue.put(root)
        max_depth = 0
        while not my_queue.empty():
            cur_size = my_queue.qsize()
            max_depth += 1
            while cur_size > 0:
                cur = my_queue.get()
                cur_size -= 1
                if cur.left is not None:
                    my_queue.put(cur.left)
                if cur.right is not None:
                    my_queue.put(cur.right)
        else:
            return max_depth

    def max_depth_recursive(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        if left_depth > right_depth:
            return left_depth + 1
        return right_depth + 1