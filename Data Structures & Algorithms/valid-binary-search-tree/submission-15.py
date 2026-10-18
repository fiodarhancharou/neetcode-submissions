# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], l_bound=float("-inf"), r_bound=float("inf")) -> bool:
        if not root:
            return True
        if not l_bound < root.val < r_bound:
            return False
        return self.isValidBST(root.left, l_bound, root.val) and self.isValidBST(root.right, root.val, r_bound)