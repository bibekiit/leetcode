# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        if root is None:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1
    def getHeight(self, root):
        if root is None:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))