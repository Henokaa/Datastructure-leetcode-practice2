# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.mx = 0
        def dfs(root):
            if not root:
                return (1001, 0)
            left = dfs(root.left)
            right = dfs(root.right)
            
            
            
            count_left = 0
            if left[0] == root.val:
                count_left = max(count_left, left[1])
            
            count_right = 0
            if right[0] == root.val:
                count_right = max(count_right, right[1])
            
            # print(root.val, left, right, count_left, count_right)
            
            self.mx = max(self.mx, count_left + count_right + 1)
            return (root.val, max(count_right, count_left) + 1)
        
        if not root:
            return 0
        dfs(root)
        return self.mx - 1