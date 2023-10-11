# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, path):
            if not root:
                return
            
            path.append(root.val)
            if not root.left and not root.right and sum(path) == targetSum:
                ans.append(path.copy())
            
            left = dfs(root.left, path)
            right = dfs(root.right, path)
            path.pop()
        
            
        ans = []
        dfs(root, [])
        return ans