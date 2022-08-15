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
        if not root and subRoot:
            return False
        if not root and not subRoot:
            return False
        if root.val == subRoot.val:
            self.dfs(root, subRoot)
        if self.dfs(root, subRoot):
            return True
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right
        
    def dfs(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        left = self.dfs(root.left, subRoot.left)
        right = self.dfs(root.right, subRoot.right)

        return left and right
    
''' Time-complexity = o(s * r) because the values can be repeated then the childerens will be checked for every same node so approximate to this
space-complexity = o(s + n) the biggest one o(s)'''
