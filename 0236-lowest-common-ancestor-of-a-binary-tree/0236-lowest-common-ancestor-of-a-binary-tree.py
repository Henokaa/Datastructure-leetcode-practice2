# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        l & r == True
        root.value == p and l or r True
        
        '''
        self.answer = None
        def dfs(root):
            if not root:
                return False
            
            left = dfs(root.left)
            right = dfs(root.right)
            # print(root.val, left, right)
            if left == True and right == True:
                self.answer = root
                return False
            
            if root.val == p.val or root.val == q.val:
                if left == True or right == True:
                    self.answer = root
                    return False
            
            if root.val == p.val or root.val == q.val:
                return True
            return left or right
            
        
        dfs(root)
        return self.answer