# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot and root:
            return True
        if subRoot and not root:
            return False
        if not subRoot and not root:
            return True
        if self.helper(root, subRoot):
            return True
         #can't be if root.val == subRoot.val:
         #              return self.helper(root, subRoot)
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        
        return left or right
    
    def helper(self, root, subroot):
        if not root and not subroot:
            return True
        if not subroot or not root:
            return False
        if root.val != subroot.val:
            return False
        left = self.helper(root.left, subroot.left)
        right = self.helper(root.right, subroot.right)
        
        return left and right
            
                
        