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
            
            if left > root.val > right:
                r = dfs(left,root.right,root.val)
                l = dfs(root.val, root.left, right)
                return l and r
            else:
                return False
        
        if not dfs(float("INF"), root, float("-INF")):
            return False
        return True
'''Brute force- for every node, check if on the left side of the node is less than the root and on thwe right greater o(n^2)
optimized - o(n)'''
    