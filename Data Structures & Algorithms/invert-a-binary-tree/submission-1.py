# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        queue = [root]
        while queue:
            level_queue = []
            for node in queue:
                node.left, node.right = node.right, node.left
                if node.left:
                    level_queue.append(node.left)
                if node.right:
                    level_queue.append(node.right)
            queue = level_queue

        return root