# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        '''
        left 
        right
        
        total = 1
        if root.val == left[0]
            total += 1
        if root.val == right[0]
            total += 1
        
        return (root.val, total)
        '''
        self.max_total = 1
        def dfs(root):
            if not root:
                return (None, 0)
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            total_left = 1
            total_right = 1
            total = 1
            if root.val == left[0]:
                total_left += left[1]
                total += left[1]
            
            if root.val == right[0]:
                total_right += right[1]
                total += right[1]
                
            self.max_total = max(self.max_total, total)
            temp = max(total_left, total_right)
            return (root.val, temp)
        
        dfs(root)
        return self.max_total - 1
        