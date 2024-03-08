# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, path):
            if not root:
                return False
            path = path + root.val
            if root.left == None and root.right == None and path == targetSum:
                return True
            
            left = dfs(root.left, path)
            right = dfs(root.right, path)
            return left or right
            
            
            
        return dfs(root, 0)
        