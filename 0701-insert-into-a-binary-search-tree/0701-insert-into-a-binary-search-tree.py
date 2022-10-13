# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.node = TreeNode(val)
        if not root:
            root = self.node
        def dfs(root):
            if val > root.val:
                if not root.right:
                    root.right = self.node
                    return
                dfs(root.right)
            if val < root.val:
                if not root.left:
                    root.left = self.node
                    return
                dfs(root.left)
                
        dfs(root)
        return root        
        