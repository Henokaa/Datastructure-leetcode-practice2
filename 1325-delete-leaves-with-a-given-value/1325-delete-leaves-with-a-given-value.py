# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        '''
        dfs()
        if 
            return
        left = 
        right =
        
        if left & right & val:
            return None
            
        return root
        
        '''
        
        def dfs(root):
            if not root:
                return None
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left == None and right == None and root.val == target:
                return None
            
            root.left = left
            root.right = right
            
            return root
        
        return dfs(root)