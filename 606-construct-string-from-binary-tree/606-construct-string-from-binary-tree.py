# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.s = ""
        
        def preorder(root):
            if not root:
                return
            
            self.s += "("
            self.s += str(root.val)
            
            if not root.left and root.right:
                self.s += "()"
                
            preorder(root.left)
            preorder(root.right)
            
            self.s += ")"
        preorder(root)
        length = len(self.s) 
        return self.s[1: length - 1]
        