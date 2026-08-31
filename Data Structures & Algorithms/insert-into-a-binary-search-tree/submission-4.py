# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, val):
        if not root:
            return

        if val < root.val:
            if root.left:
                # if root.left.val < self.val < root.val:
                self.traverse(root.left, val)
            else:
                root.left = TreeNode(val)
        else:
            # if root.val < self.val < root.right.val::
            if root.right:
                self.traverse(root.right, val)
            else:
                root.right = TreeNode(val)

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        self.traverse(root, val)
        return root