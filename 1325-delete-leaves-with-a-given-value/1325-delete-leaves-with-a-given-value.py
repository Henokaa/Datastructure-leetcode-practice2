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
            left
            right
            
            if not left and not right
                return None
            
        '''
        
                
        def dfs(root):
            if not root:
                return None
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            root.left = left
            root.right = right
            
            if root.left == None and root.right == None and root.val == target:
                # print("Yes")
                return None
            
            return root
        
        return dfs(root)
        
        