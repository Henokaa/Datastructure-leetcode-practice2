# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        if l == True and r == True
        
        if root.val == p and (l ==True or r == True)
        
        if root.val == q and (l ==True or r == True)
        
        if root.val == p.val:
            return true
        
        
        '''
        self.answer = None
        self.p_val = None
        self.q_val = None
        def dfs(root):
            if not root:
                return False
 
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left == True and right == True:
                self.answer = root
                return False
            
            if root.val == p.val and (left == True or right == True):
                self.answer = root
                return False
            
            if root.val == q.val and (left == True or right == True):
                self.answer = root
                return False
            
            if root.val == p.val or root.val == q.val:
                # print("A",root.val)
                return True
            
            return left or right
        
        dfs(root)
        return self.answer