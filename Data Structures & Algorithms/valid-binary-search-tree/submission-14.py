# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], bound=(float('-inf'), float('inf'))) -> bool:
        if not root:
            return True
        
        if not bound[0] < root.val < bound[1]:
            return False
        return self.isValidBST(root.left, (bound[0], root.val)) and self.isValidBST(root.right, (root.val, bound[1]))
        
