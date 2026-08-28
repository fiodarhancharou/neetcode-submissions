class Solution:
    def dfs(self, preorder, inorder, pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end or in_start > in_end:
            return None
        
        node = TreeNode(preorder[pre_start])
        ind = self.precomp[node.val]
        
        # Size of left subtree
        left_size = ind - in_start
        
        # Left subtree: preorder[pre_start+1 : pre_start+1+left_size]
        node.left = self.dfs(preorder, inorder, pre_start + 1, pre_start + left_size, in_start, ind - 1)
        
        # Right subtree: preorder[pre_start+1+left_size : pre_end+1]
        node.right = self.dfs(preorder, inorder, pre_start + left_size + 1, pre_end, ind + 1, in_end)
        
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.precomp = {val: i for i, val in enumerate(inorder)}
        return self.dfs(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)