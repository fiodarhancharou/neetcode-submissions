# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            row_queue = []
            row_res = []
            for node in queue:
                if node:
                    row_res.append(node.val)
                if node.left:
                    row_queue.append(node.left)
                if node.right:
                    row_queue.append(node.right)
            if row_res:
                res.append(row_res)
            queue = row_queue
        return res

