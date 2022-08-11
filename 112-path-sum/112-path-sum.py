# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, cur):
            if not root:
                return False  # but when it is and it would of been True because if once T and false always false
            cur += root.val
            if not root.left and not root.right and targetSum == cur:
                return True
            # else: at the end it return true or comes to this line to return false
            return dfs(root.left, cur) or dfs(root.right, cur)
        
        return dfs(root, 0)
