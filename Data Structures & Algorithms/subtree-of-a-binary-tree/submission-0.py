# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Basic conditions
        if not subRoot:  # An empty subtree is always a subtree
            return True
        if not root:  # If root is empty and subRoot is not, it's not a subtree
            return False

        # Check if they are the same tree
        if self.sameTree(root, subRoot):
            return True

        # Check the left and right subtrees recursively
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If both nodes are None, they are the same
        if not root and not subRoot:
            return True

        # If one is None or their values are not the same, return False
        if not root or not subRoot or root.val != subRoot.val:
            return False

        # Recursively check left and right children
        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
