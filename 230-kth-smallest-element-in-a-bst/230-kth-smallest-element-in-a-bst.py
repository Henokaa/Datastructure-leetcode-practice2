# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''iteration '''
        n = 0
        stack = []
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right
#         order = []
#         def dfs(root):
#             if not root:
#                 return 
#             left = dfs(root.left)
#             order.append(root.val)
#             right = dfs(root.right)
        
#         dfs(root)
        
#         return order[k-1]
