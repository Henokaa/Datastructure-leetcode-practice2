# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        '''
        left
        right
        
        return coin left
        move
        
        return abs(left) + abs(right) - 1 
        '''
        self.move = 0
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            self.move += abs(left) + abs(right)
            
            coins = root.val + left + right - 1 
            
            return coins
        
        dfs(root)
        return self.move