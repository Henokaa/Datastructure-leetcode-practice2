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
            count = 1
            res = 1
            l = dfs(root.left)
            if l[0] == root.val:
                count += l[1]
                res = max(res, l[1]+1)
                    
            r = dfs(root.right)
            if r[0] == root.val:
                count += r[1]
                res = max(res, r[1]+1)
            
            # count += 1
            
            self.mx = max(self.mx, count)
            
            return (root.val, res)
        
        dfs(root)
        if not root:
            return 0
        return self.mx -1 