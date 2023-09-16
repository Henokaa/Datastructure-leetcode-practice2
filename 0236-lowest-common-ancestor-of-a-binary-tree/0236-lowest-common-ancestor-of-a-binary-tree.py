# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        self.temp = None
        def dfs(root):
            if not root:
                return False
            if root.val == p.val or root.val == q.val:
                self.temp = root
                return True
            left = None
            right = None
            
            left = dfs(root.left)
                
            
            right = dfs(root.right)
                
            # print(left, right, (root.val))
            
            if left == True and right == True:
                self.ans = root
            
            
            return left or right
        
        dfs(root)
        # print(self.ans, self.temp)
        if self.ans != None:
            return self.ans
        if self.temp != None:
            return self.temp