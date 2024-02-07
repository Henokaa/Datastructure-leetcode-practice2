# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        
        '''
    
        def dfs(root):
            if not root:
                return 
            
            if (p.val < root.val < q.val) or (q.val < root.val < p.val):
                self.answer = root
                return 
            
            if p.val == root.val:
                self.answer = p
                return 
            
            if q.val == root.val:
                self.answer = q
                return  
            
            if p.val > root.val and q.val > root.val:
                dfs(root.right)
            
            if p.val < root.val and q.val < root.val:
                dfs(root.left)
            
            return 
                
        
        # print(p)
        dfs(root)
        return self.answer
        