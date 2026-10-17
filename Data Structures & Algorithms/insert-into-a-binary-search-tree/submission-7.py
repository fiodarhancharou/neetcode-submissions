# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        print(root.val)
        self.dfs(root.right)

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        branch_map = {"left": root.left, "right": root.right}
        next_node_key = "left" if root.val > val else "right"
        if branch_map[next_node_key]:
            self.insertIntoBST(branch_map[next_node_key], val)
        else:
            next_node = TreeNode(val)
            if next_node_key == "left":
                root.left = next_node
            else:
                root.right = next_node
        return root