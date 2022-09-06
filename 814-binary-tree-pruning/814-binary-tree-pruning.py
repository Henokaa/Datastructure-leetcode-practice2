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
            result = left or right or root.val
            if not left:
                root.left = None
            if not right:
                root.right = None
            if not result:
                return False
            else:
                return True
            
        res = prune(node)
        if not res:
            node = None
        return node
        