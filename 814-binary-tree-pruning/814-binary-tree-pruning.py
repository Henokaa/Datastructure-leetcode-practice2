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
            left = prune(root.left)
            right = prune(root.right)
            
            if not left:
                root.left = None
            if not right:
                root.right = None
            return left or right or root.val
            
        res = prune(node)
        if not res:
            node = None
        return node
        