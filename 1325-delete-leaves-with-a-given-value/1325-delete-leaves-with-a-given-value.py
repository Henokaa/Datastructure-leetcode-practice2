# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        '''
        dfs
            left
            right
            
            
        '''
        
        def dfs(root):
            if not root:
                return None
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left == None and right == None and root.val == target:
                # print(root.val)
                return None
            
            root.left = left   # Very hard to remeber
            root.right = right  # Very hard to remeber
            
            return root
            
        return dfs(root)
        