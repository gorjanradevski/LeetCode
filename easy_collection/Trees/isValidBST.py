# 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_valid_util(self, node, min_val, max_val):
        if node is None:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        if not self.is_valid_util(node.right, node.val, max_val):
            return False

        if not self.is_valid_util(node.left, min_val, node.val):
            return False

        return True

    def is_valid_iter(self, root):
        if root is None:
            return True
        stack = [(root, float("-inf"), float("inf"))]
        while len(stack) > 0:
            node, min_val, max_val = stack.pop()
            if node is None:
                continue
            if node.val <= min_val or node.val >= max_val:
                return False
            stack.append((node.right, node.val, max_val))
            stack.append((node.left, min_val, node.val))
        return True

    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid_util(root, float("-inf"), float("inf"))
