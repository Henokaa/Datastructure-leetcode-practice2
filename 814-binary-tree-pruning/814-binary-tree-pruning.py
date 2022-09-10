# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def prune(root):
            if not root:
                return False
            L = prune(root.left)
            R = prune(root.right)
            s = L or R or root.val
            if not L:
                root.left = None
            if not R:
                root.right = None
            
            return s
        
        if not prune(node):
            node = None
        
        return node
        