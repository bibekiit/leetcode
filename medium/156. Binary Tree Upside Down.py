'''
Given the root of a binary tree, turn the tree upside down and return the new root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.
'''

# Solution 1: Recursion
#
# Time Complexity: O(n)
#
# Space Complexity: O(n)

from typing import Optional

class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):

        self.val = val

        self.left = left

        self.right = right

class Solution:

    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root or not root.left:

            return root

        new_root = self.upsideDownBinaryTree(root.left)

        # We need to make sure that the right child of the new root is the original root



        root.left.left = root.right

        root.left.right = root

        root.left = None

        root.right = None

        return new_root
    
# Solution 2: Iteration
#
# Time Complexity: O(n)

# Space Complexity: O(1)

class Solution:
    
        def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
            curr = root
    
            # prev is the new root
            prev = None
    
            # next is the new left child
            next = None
    
            # temp is the new right child
            temp = None
    
            while curr:
    
                next = curr.left
    
                curr.left = temp
    
                temp = curr.right
    
                curr.right = prev
    
                prev = curr
    
                curr = next
    
            return prev