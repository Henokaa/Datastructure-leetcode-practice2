# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)  
            right = dfs(root.right)
            if abs(left - right) > 1:
                self.isbal = False
            return 1 + max(left, right)
        self.isbal = True
        dfs (root)
        return self.isbal
        