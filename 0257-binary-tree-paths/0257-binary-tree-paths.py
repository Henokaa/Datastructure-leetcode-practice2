# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def dfs(root, path):
            if not root:
                return 
            path.append(root.val)
            if not root.left and not root.right:
                ans.append('->'.join(map(str, path.copy())))
            
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()

            return 
        
        ans = []
        dfs(root, [])
        return ans