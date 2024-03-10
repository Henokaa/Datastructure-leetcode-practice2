# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        left
        right
        
        total = root.val
        if left > 0
            
        if right > 0
        
        
        return max(left, right)
        '''
        self.answer = float('-inf')
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            total = root.val
            total_left = 0
            total_right = 0
            
            if left > 0:
                total += left
                total_left += left
            
            if right > 0:
                total += right
                total_right += right
            
            self.answer = max(self.answer, total)
            temp = max(total_left+root.val, total_right+root.val)
            
            return temp
            
        dfs(root)
        return self.answer