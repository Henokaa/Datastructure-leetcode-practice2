# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return False
            
            if root.val == p.val or root.val == q.val:
                self.ans2 = root
                return True
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left == True and right == True:
                self.ans = root
            
            return left or right
        
        self.ans = float('-inf')
        self.ans2 = 0
        dfs(root)
        
        if self.ans == float('-inf'):
            return self.ans2
        return self.ans
        
        
             
                