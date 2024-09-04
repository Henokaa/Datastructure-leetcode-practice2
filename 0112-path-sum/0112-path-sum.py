# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.ans = False
        def dfs(root, pathSum):
            if not root:
                return None
            
            pathSum += root.val
            # print(pathSum)
            left = dfs(root.left, pathSum)
            right = dfs(root.right, pathSum)
            
            
            if left == None and right == None:
                # print("Leaf", pathSum)
                if pathSum == targetSum:
                    self.ans = True
            pathSum -= root.val
            
            return root
                
        
        dfs(root, 0)
        
        return self.ans