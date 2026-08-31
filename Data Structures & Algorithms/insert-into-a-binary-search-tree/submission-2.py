# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, left=float("-inf"), right=float("inf")):
        if not root:
            return

        if self.val < root.val:
            if root.left:
                # if root.left.val < self.val < root.val:
                self.traverse(root.left, left, root.val)
            else:
                root.left = TreeNode(self.val)
        else:
            # if root.val < self.val < root.right.val::
            if root.right:
                self.traverse(root.right, root.val, right)
            else:
                root.right = TreeNode(self.val)
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        self.val = val
        self.traverse(root)
        return root