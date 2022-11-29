# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.mx = 0
        def dfs(rt, prev):
            if not rt:
                return 0
            
            left = dfs(rt.left, rt.val)
            right = dfs(rt.right, rt.val)
            self.mx = max(left + right + 1, self.mx)
            ret = 0
            if rt.val == prev:
                ret = max(left, right) + 1
            return ret
        
        if not root:
            return 0
        
        dfs(root, -1001)
        return self.mx - 1