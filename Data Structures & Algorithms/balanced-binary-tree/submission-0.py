# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def treeDepth(self, root):
        if not root:
            return 0
        return max(self.treeDepth(root.left), self.treeDepth(root.right)) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        elif abs(self.treeDepth(root.left) - self.treeDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

        
