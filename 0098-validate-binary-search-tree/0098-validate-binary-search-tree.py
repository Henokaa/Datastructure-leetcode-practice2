# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, root, right):
            if not root:
                return True
            if left < root.val < right:
                left = dfs(left, root.left, root.val)
                right = dfs(root.val, root.right,  right)
                return left and right
            else:
                return False
            
        return dfs(float("-INF"),root, float("INF"))