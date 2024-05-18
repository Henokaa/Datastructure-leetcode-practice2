# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        '''
        leaf and == target dealt
        
        dfs
            
        '''
        
        def dfs(root):
            if root is None:
                return
            left = dfs(root.left)
            right = dfs(root.right)
            # print(root.val)
            if root.left is not None and root.left.val == -1:
                # print("yes")
                root.left = None
            
            if root.right is not None and root.right.val == -1:
                root.right = None
            
            if root.left is None and root.right is None and root.val == target:
                # print("yes_2")
                root.val = -1
        
        dfs(root)
        if root.val == -1:
            root = None
        return root
                
                