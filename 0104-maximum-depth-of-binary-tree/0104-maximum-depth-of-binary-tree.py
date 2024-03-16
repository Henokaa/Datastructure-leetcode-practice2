# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        maximum = 0
        def dfs(root, level):
            if not root:
                return
            nonlocal maximum
            maximum = max(maximum, level)
            
            left = dfs(root.left, level + 1)
            right = dfs(root.right, level + 1)
        
        dfs(root, 1)
        return maximum
        
        