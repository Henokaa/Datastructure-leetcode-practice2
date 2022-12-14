# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            mx = max(left, right)
            
            if left >= 0 and right >= 0:
                # print(left, right, root.val)
                self.ans = max(self.ans, left + right + root.val)
            elif left <= 0 and right >= 0:
                self.ans = max(self.ans, right + root.val)
            elif left >= 0 and right <= 0:
                self.ans = max(self.ans, left + root.val)
            elif left <= 0 and right <= 0:
                self.ans = max(self.ans, root.val)
                
            if mx < 0:
                mx = 0
            return mx + root.val

        self.ans = float('-inf')
        temp = dfs(root) 
        return self.ans