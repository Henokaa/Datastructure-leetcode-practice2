# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        s = ""
        def strr(root):

            if not root:
                return ""
            if not root.left and root.right:
                return "(" + str(root.val) + "()" + strr(root.right) + ")"

            return "(" + str(root.val) + strr(root.left) + strr(root.right) + ")"
            
        s = strr(root)
        length = len(s)
        
        return s[1:length- 1]
        
        